from copy import deepcopy
from typing import Tuple, List, Dict, Any

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import Simulation
from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import Subgraph


class V4Simulation(Simulation):


    def _run_chunk(self,
                   percent_adopt_trials: List[Tuple[float, int]],
                   # MUST leave as false. _get_mp_results depends on this
                   # This should be fixed and this comment deleted
                   single_proc: bool = False
                   ) -> Tuple[Subgraph, ...]:
        """Runs a chunk of trial inputs"""

        # Engine is not picklable or dillable AT ALL, so do it here
        # (after the multiprocess process has started)
        # Changing recursion depth does nothing
        # Making nothing a reference does nothing
        engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                                GraphCls=SimulationEngine,
                                ).run(tsv_path=None)
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

                print(
                    f"{percent_adopt * 100}% {scenario.graph_label}, #{trial}",
                    end="                             " + "\r")

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
                    scenario.pre_aggregation_hook(**kwargs)
                    # Save all engine run info
                    # The reason we aggregate info right now, instead of saving
                    # the engine and doing it later, is because doing it all
                    # in RAM is MUCH faster, and speed is important
                    self._aggregate_engine_run_data(subgraphs, **kwargs)

                    # By default, this is a no op
                    scenario.post_propagation_hook(**kwargs)
            # Reset scenario for next round of trials
            prev_scenario = None
        return subgraphs

    # TODO: Currently has no changes compared to parent
    def _aggregate_engine_run_data(self,
                                   subgraphs: Tuple[Subgraph, ...],
                                   **kwargs):
        """For each subgraph, aggregate data

        Some data aggregation is shared to speed up runs
        For example, traceback might be useful across
        Multiple subgraphs
        """
        print("Inside _aggregate_engine_run_data in V4Simulation")
        shared_data: Dict[Any, Any] = dict()
        for subgraph in subgraphs:
            print(subgraph)
            subgraph.aggregate_engine_run_data(shared_data, **kwargs)
