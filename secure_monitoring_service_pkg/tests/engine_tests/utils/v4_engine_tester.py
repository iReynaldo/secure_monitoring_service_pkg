from copy import deepcopy
from typing import Dict, Any
from pathlib import Path
import random

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTester
from bgp_simulator_pkg import Outcomes

from .v4_diagram import V4Diagram

from secure_monitoring_service_pkg.simulation_framework.subgraphs.v4_subgraph import (
    V4Subgraph,
)
from ....simulation_framework.scenarios.hijack_scenarios import (
    SubprefixAutoImmuneScenario,
)
from ....simulation_framework.scenarios.hijack_scenarios import (
    V4SubprefixHijackScenario,
)
from ....simulation_framework.scenarios.hijack_scenarios import (
    ArtemisSubprefixHijackScenario,
)


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
        # Set Random seed
        random.seed(0)

        # Get a fresh copy of the scenario
        scenario = deepcopy(self.conf.scenario)
        # Get's an engine that has been set up
        engine = self._get_engine(scenario)
        # Run engine
        for propagation_round in range(self.conf.propagation_rounds):
            engine.run(propagation_round=propagation_round, scenario=scenario)
            kwargs = {
                "engine": engine,
                "scenario": scenario,
                "propagation_round": propagation_round,
            }
            scenario.pre_aggregation_hook(**kwargs)

        prefix_outcomes: Dict[str, Dict[AS, Outcomes]] = dict()
        prefix_outcomes_yaml: Dict[str, Dict[AS, Outcomes]] = dict()
        for attacker_ann in scenario.get_attacker_announcements_for_origin():
            # Get traceback results {AS: Outcome}
            outcomes, traceback_asn_outcomes = V4Subgraph()._get_engine_outcomes(
                engine, scenario, attacker_ann
            )
            # Create Shared data
            shared_data: Dict[Any, Any] = dict()
            # Update outcomes if reconnections via relays can be made
            if scenario.relay_asns and (
                isinstance(scenario, SubprefixAutoImmuneScenario)
                or isinstance(scenario, V4SubprefixHijackScenario)
            ):
                # Add relay prefix data to shared data
                shared_data["relay_prefixes"] = scenario.relay_prefixes
                V4Subgraph()._recalculate_outcomes_with_relays(
                    scenario,
                    engine,
                    attacker_ann,
                    outcomes,
                    traceback_asn_outcomes,
                    shared_data,
                    track_relay_usage=True,
                )
            prefix_outcomes[attacker_ann.prefix] = outcomes
            # Convert this to just be {ASN: Outcome} (Not the AS object)
            outcomes_yaml = {as_obj.asn: result for as_obj, result in outcomes.items()}
            prefix_outcomes_yaml[attacker_ann.prefix] = outcomes_yaml

            # Add additional things to shared_data for system test checking
            if scenario.avoid_lists:
                for prefix in scenario.avoid_lists:
                    shared_data[f"avoid_list_for_{prefix}"] = sorted(
                        scenario.avoid_lists[prefix]
                    )

            # Verify the Avoid List
            if scenario.has_rovsms_ases:
                V4Subgraph().verify_avoid_list(
                    engine,
                    scenario,
                    outcomes,
                    shared_data,
                    traceback_asn_outcomes,
                    trigger_assert=False,
                )

        # Aggregate outcomes
        V4Subgraph()._add_traceback_to_shared_data(
            shared_data, engine, scenario, prefix_outcomes
        )

        # By default, this is a no op
        scenario.post_propagation_hook(**kwargs)  # Clears scenario data

        # Store engine and traceback YAML
        self._store_yaml(engine, prefix_outcomes_yaml, shared_data)

        # Create Diagrams
        for prefix in prefix_outcomes:
            # Create diagrams before the test can fail
            self._generate_diagrams(shared_data, prefix)

            # Compare the YAML's together
            self._compare_yaml(prefix)

    def _store_yaml(self, engine, prefix_outcomes, shared_data):
        """Stores YAML for the engine, outcomes, and shared_data.

        If ground truth doesn't exist, create it
        """

        for prefix, outcomes in prefix_outcomes.items():
            # Save engine
            self.codec.dump(engine, path=self.get_engine_guess_path(prefix))
            # Save engine as ground truth if ground truth doesn't exist
            if not self.get_engine_ground_truth_path(prefix).exists() or self.overwrite:
                self.codec.dump(engine, path=self.get_engine_ground_truth_path(prefix))
            # Save outcomes
            self.codec.dump(outcomes, path=self.get_outcomes_guess_path(prefix))
            # Save outcomes as ground truth if ground truth doesn't exist
            if (
                not self.get_outcomes_ground_truth_path(prefix).exists()
                or self.overwrite
            ):
                self.codec.dump(
                    outcomes, path=self.get_outcomes_ground_truth_path(prefix)
                )
            self.codec.dump(shared_data, path=self.get_shared_data_guess_path(prefix))
            # Save shared_data as ground truth if ground truth doesn't exist
            if (
                not self.get_shared_data_ground_truth_path(prefix).exists()
                or self.overwrite
            ):
                self.codec.dump(
                    shared_data, path=self.get_shared_data_ground_truth_path(prefix)
                )

    def _compare_yaml(self, prefix):
        """Compares YAML for ground truth vs guess for engine and outcomes"""

        # Compare Engine
        engine_guess = self.codec.load(self.get_engine_guess_path(prefix))
        engine_gt = self.codec.load(self.get_engine_ground_truth_path(prefix))
        assert engine_guess == engine_gt
        # Compare outcomes
        outcomes_guess = self.codec.load(self.get_outcomes_guess_path(prefix))
        outcomes_gt = self.codec.load(self.get_outcomes_ground_truth_path(prefix))
        assert outcomes_guess == outcomes_gt
        # Compare shared_data
        shared_data_guess = self.codec.load(self.get_shared_data_guess_path(prefix))
        shared_data_gt = self.codec.load(self.get_shared_data_ground_truth_path(prefix))
        assert shared_data_guess == shared_data_gt

    def _generate_diagrams(self, shared_data, prefix):
        """Generates diagrams"""

        # Load engines
        engine_guess = self.codec.load(self.get_engine_guess_path(prefix))
        engine_gt = self.codec.load(self.get_engine_ground_truth_path(prefix))
        # Load outcomes
        outcomes_guess = self.codec.load(self.get_outcomes_guess_path(prefix))
        outcomes_gt = self.codec.load(self.get_outcomes_ground_truth_path(prefix))

        # Draw Graphs
        prefix_without_slash = prefix.replace("/", "_")
        # Write guess graph
        V4Diagram().generate_as_graph(
            engine_guess,
            self.conf.scenario,  # type: ignore
            outcomes_guess,
            f"({self.conf.name} Guess)\n"  # type: ignore
            f"{self.conf.desc}\n"  # type: ignore
            f"Traceback for {prefix}",  # type: ignore
            shared_data,
            path=self.test_dir / f"guess_{prefix_without_slash}.gv",
            view=False,
        )
        # Write ground truth graph
        V4Diagram().generate_as_graph(
            engine_gt,
            self.conf.scenario,  # type: ignore
            outcomes_gt,
            f"({self.conf.name} Ground Truth)\n"  # type: ignore
            f"{self.conf.desc}\n"  # type: ignore
            f"Traceback for {prefix}",
            shared_data,
            path=self.test_dir / f"ground_truth_{prefix_without_slash}.gv",
            view=False,
        )

    #########
    # Paths #
    #########

    def get_engine_ground_truth_path(self, prefix) -> Path:
        """Returns the path to the engine's ground truth YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"engine_gt_{prefix_without_slash}.yaml"

    def get_engine_guess_path(self, prefix) -> Path:
        """Returns the path to the engine's guess YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"engine_guess_{prefix_without_slash}.yaml"

    def get_outcomes_ground_truth_path(self, prefix) -> Path:
        """Returns the path to the outcomes ground truth YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"outcomes_gt_{prefix_without_slash}.yaml"

    def get_outcomes_guess_path(self, prefix) -> Path:
        """Returns the path to the outcomes guess YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"outcomes_guess_{prefix_without_slash}.yaml"

    def get_shared_data_ground_truth_path(self, prefix) -> Path:
        """Returns the path to the shared_data ground truth YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"shared_data_gt_{prefix_without_slash}.yaml"

    def get_shared_data_guess_path(self, prefix) -> Path:
        """Returns the path to the shared_data guess YAML"""

        prefix_without_slash = prefix.replace("/", "_")
        return self.test_dir / f"shared_data_guess_{prefix_without_slash}.yaml"
