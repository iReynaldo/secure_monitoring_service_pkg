from copy import deepcopy
from typing import Dict, Any

from bgp_simulator_pkg import EngineTester
from bgp_simulator_pkg import Subgraph

from .v4_diagram import V4Diagram

from secure_monitoring_service_pkg.simulation_framework.v4_subgraph import V4Subgraph

class V4EngineTester(EngineTester):

    def test_engine(self):
        """Tests an engine run

        Takes in a scenario (initialized with adopt ASN, atk and vic ASN,
        and a graph
        The scenario + graph are used to build and seed the engine
        After the engine is seeded, the engine is run
        Data is collected from the engine
        The engine and traceback are output to YAML
        We then compare the current run's traceback and engine
            to the ground truth
        """

        # Get a fresh copy of the scenario
        scenario = deepcopy(self.conf.scenario)
        # Get's an engine that has been set up
        engine = self._get_engine(scenario)
        # Run engine
        for propagation_round in range(self.conf.propagation_rounds):
            engine.run(propagation_round=propagation_round,
                       scenario=scenario)
            kwargs = {"engine": engine,
                      "scenario": scenario,
                      "propagation_round": propagation_round}
            scenario.pre_aggregation_hook(**kwargs)

            # Create Shared data
            shared_data: Dict[Any, Any] = dict()
            # Add additional things to shared_data for system test checking
            if scenario.avoid_lists:
                for prefix in scenario.avoid_lists:
                    shared_data[f"avoid_list_for_{prefix}"] = sorted(scenario.avoid_lists[prefix])

            # By default, this is a no op
            scenario.post_propagation_hook(**kwargs)

        # Get traceback results {AS: Outcome}
        outcomes, traceback_asn_outcomes = V4Subgraph()._get_engine_outcomes(engine, scenario)
        # Convert this to just be {ASN: Outcome} (Not the AS object)
        outcomes_yaml = {as_obj.asn: result for as_obj, result in outcomes.items()}
        # Get shared_data
        V4Subgraph()._add_traceback_to_shared_data(shared_data,
                                                   engine,
                                                   scenario,
                                                   outcomes)


        # Store engine and traceback YAML
        self._store_yaml(engine, outcomes_yaml, shared_data)
        # Create diagrams before the test can fail
        self._generate_diagrams(shared_data)
        # Compare the YAML's together
        self._compare_yaml()

    def _generate_diagrams(self, shared_data):
        """Generates diagrams"""

        # Load engines
        engine_guess = self.codec.load(self.engine_guess_path)
        engine_gt = self.codec.load(self.engine_ground_truth_path)
        # Load outcomes
        outcomes_guess = self.codec.load(self.outcomes_guess_path)
        outcomes_gt = self.codec.load(self.outcomes_ground_truth_path)

        # Write guess graph
        V4Diagram().generate_as_graph(
            engine_guess,
            self.conf.scenario,  # type: ignore
            outcomes_guess,
            f"({self.conf.name} Guess)\n{self.conf.desc}",  # type: ignore,
            shared_data,
            path=self.test_dir / "guess.gv",
            view=False)
        # Write ground truth graph
        V4Diagram().generate_as_graph(
            engine_gt,
            self.conf.scenario,  # type: ignore
            outcomes_gt,
            f"({self.conf.name} Ground Truth)\n"  # type: ignore
            f"{self.conf.desc}",  # type: ignore,
            shared_data,
            path=self.test_dir / "ground_truth.gv",
            view=False)