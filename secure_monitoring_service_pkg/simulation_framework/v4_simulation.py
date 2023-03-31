from copy import deepcopy
from typing import Tuple, List, Dict, Any
from pathlib import Path
from tempfile import TemporaryDirectory
import json
from shutil import make_archive


from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import Simulation
from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import Subgraph


class V4Simulation(Simulation):

    def run(self, experiment_settings_to_save=None):
        """Runs the simulation and write the data"""

        self._get_data()
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

    pass
