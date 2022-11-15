from copy import deepcopy
from typing import Dict, Any

from bgp_simulator_pkg import EngineTester
from bgp_simulator_pkg import Subgraph

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
            # By default, this is a no op
            scenario.post_propagation_hook(**kwargs)

        # Get traceback results {AS: Outcome}
        outcomes, traceback_asn_outcomes = V4Subgraph()._get_engine_outcomes(engine, scenario)
        # Convert this to just be {ASN: Outcome} (Not the AS object)
        outcomes_yaml = {as_obj.asn: result for as_obj, result in outcomes.items()}
        # Get shared_data
        shared_data: Dict[Any, Any] = dict()
        V4Subgraph()._add_traceback_to_shared_data(shared_data,
                                                   engine,
                                                   scenario,
                                                   outcomes)
        # Store engine and traceback YAML
        self._store_yaml(engine, outcomes_yaml, shared_data)
        # Create diagrams before the test can fail
        self._generate_diagrams()
        # Compare the YAML's together
        self._compare_yaml()