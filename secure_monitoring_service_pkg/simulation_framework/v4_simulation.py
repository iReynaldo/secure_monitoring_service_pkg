from typing import List, Optional, Tuple, Union
from pathlib import Path
from tempfile import TemporaryDirectory
import json
from shutil import make_archive
from datetime import datetime
import random
from copy import deepcopy



from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import Simulation
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Subgraph
from bgp_simulator_pkg import SpecialPercentAdoptions
from bgp_simulator_pkg import SubprefixHijack
from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import BGPSimpleAS

####################
# Constants
####################

CAIDA_CACHE_DIR = "~/tmp/caida_collector_cache"
CAIDA_CACHE_TSV = "~/tmp/caida_collector.tsv"

class V4Simulation(Simulation):

    def __init__(self,
                 percent_adoptions: Tuple[
                     Union[float, SpecialPercentAdoptions], ...] = (
                         .05, .1, .3, .5, .8),
                 scenarios: Tuple[Scenario, ...] = tuple(
                     [SubprefixHijack(AdoptASCls=x)  # type: ignore
                      for x in [ROVSimpleAS]]
                 ),
                 subgraphs: Optional[Tuple[Subgraph, ...]] = None,
                 num_trials: int = 2,
                 propagation_rounds: int = 1,
                 output_path: Path = Path("/tmp/graphs"),
                 parse_cpus: int = 8,
                 python_hash_seed: Optional[int] = None,
                 caida_topology_date: str = None,
                 caida_kwargs=None):
        """Downloads relationship data, runs simulation

        Graphs -> A list of graph classes
        graph_path: Where to store the graphs. Should be a .tar.gz file
        assert_pypy: Ensures you are using pypy if true
        mp_method: Multiprocessing method
        """

        if subgraphs:
            self.subgraphs: Tuple[Subgraph, ...] = subgraphs
        else:
            self.subgraphs = tuple([
                Cls() for Cls in
                Subgraph.subclasses if Cls.name])

        self.percent_adoptions: Tuple[Union[float,
        SpecialPercentAdoptions],
        ...] = percent_adoptions
        self.num_trials: int = num_trials
        self.propagation_rounds: int = propagation_rounds
        self.output_path: Path = output_path
        self.parse_cpus: int = parse_cpus
        self.scenarios: Tuple[Scenario, ...] = scenarios
        self.python_hash_seed = python_hash_seed
        self.caida_graphcls_kwargs = caida_kwargs
        self.caida_download_time = None
        # All scenarios must have a uni que graph label
        labels = [x.graph_label for x in self.scenarios]
        assert len(labels) == len(set(labels)), "Scenario labels not unique"

        # Done here so that the caida files are cached
        # So that multiprocessing doesn't interfere with one another
        if caida_topology_date:
            dl_time = datetime.strptime(caida_topology_date, '%Y.%m.%d')
            dl_time.replace(hour=0, minute=0, second=0, microsecond=0)
            self.caida_download_time = dl_time
            CaidaCollector().run(dl_time=dl_time,
                                 cache_dir=Path(CAIDA_CACHE_DIR),
                                 tsv_path=Path(CAIDA_CACHE_TSV))
        else:
            CaidaCollector().run(cache_dir=Path(CAIDA_CACHE_DIR),
                                 tsv_path=Path(CAIDA_CACHE_TSV))

    def run(self, experiment_settings_to_save=None):
        """Runs the simulation and write the data"""
        start = datetime.now()
        self._get_data()
        elapsed_time = (datetime.now() - start).total_seconds()
        if experiment_settings_to_save:
            experiment_settings_to_save["runtime_seconds"] = elapsed_time
        self._write_data(experiment_settings_to_save)

    def _write_data(self, experiment_settings_to_save=None):
        """Writes subgraphs in graph_dir"""

        # init JSON and temporary directory
        json_data = dict()
        with TemporaryDirectory() as tmp_dir:
            # Write subgraph and add data to the JSON
            for subgraph in self.subgraphs:
                subgraph.write_graphs(Path(tmp_dir))
                json_data[subgraph.name] = subgraph.data
            # Save the JSON
            with (Path(tmp_dir) / "results.json").open("w") as f:
                json.dump(json_data, f, indent=4)
            # Save experiment settings if given
            if experiment_settings_to_save:
                with (Path(tmp_dir) / "settings.json").open("w") as f:
                    json.dump(experiment_settings_to_save, f, indent=4)

            # Zip the data
            make_archive(self.output_path, "zip", tmp_dir)  # type: ignore
            print(f"\nWrote graphs to {self.output_path}.zip")

    def _run_chunk(self,
                   chunk_id: int,
                   percent_adopt_trials: List[Tuple[Union[float,
                                                    SpecialPercentAdoptions],
                                                    int]],
                   # MUST leave as false. _get_mp_results depends on this
                   # This should be fixed and this comment deleted
                   single_proc: bool = False
                   ) -> Tuple[Subgraph, ...]:
        """Runs a chunk of trial inputs"""

        # Check to enable deterministic multiprocess runs
        if self.python_hash_seed is not None and self.parse_cpus > 1:
            random.seed(chunk_id)

        # Engine is not picklable or dillable AT ALL, so do it here
        # (after the multiprocess process has started)
        # Changing recursion depth does nothing
        # Making nothing a reference does nothing
        engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                                GraphCls=SimulationEngine,
                                GraphCls_kwargs=self.caida_graphcls_kwargs,
                                ).run(dl_time=self.caida_download_time)
        # Must deepcopy here to have the same behavior between single
        # And multiprocessing
        if single_proc:
            subgraphs = deepcopy(self.subgraphs)
        else:
            subgraphs = self.subgraphs

        prev_scenario = None

        for percent_adopt, trial in percent_adopt_trials:
            for scenario in self.scenarios:

                # Deep copy scenario to ensure it's fresh
                # Since certain things like announcements change round to round
                scenario = deepcopy(scenario)

                if isinstance(percent_adopt, float):
                    print(f"{percent_adopt * 100}% "
                          f"{scenario.graph_label}, "
                          f"#{trial}",
                          end="                             " + "\r")
                elif isinstance(percent_adopt, SpecialPercentAdoptions):
                    print(f"{percent_adopt.value * 100}% "
                          f"{scenario.graph_label}, "
                          f"#{trial}",
                          end="                             " + "\r")
                else:
                    raise NotImplementedError

                # Change AS Classes, seed announcements before propagation
                scenario.setup_engine(engine, percent_adopt, prev_scenario)

                for propagation_round in range(self.propagation_rounds):
                    # Run the engine
                    engine.run(propagation_round=propagation_round,
                               scenario=scenario)

                    kwargs = {"engine": engine,
                              "percent_adopt": percent_adopt,
                              "trial": trial,
                              "scenario": scenario,
                              "propagation_round": propagation_round}

                    # Pre-aggregation Hook
                    scenario.pre_aggregation_hook(**kwargs)

                    # Save all engine run info
                    # The reason we aggregate info right now, instead of saving
                    # the engine and doing it later, is because doing it all
                    # in RAM is MUCH faster, and speed is important
                    self._aggregate_engine_run_data(subgraphs, **kwargs)

                    # By default, this is a no op
                    scenario.post_propagation_hook(**kwargs)
                prev_scenario = scenario
            # Reset scenario for next round of trials
            prev_scenario = None
        return subgraphs
