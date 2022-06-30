from pathlib import Path

from lib_bgp_simulator.tests.utils.base_graph_system_tester import BaseGraphSystemTester
from lib_bgp_simulator import enums

from lib_secure_monitoring_service import v4_scenario
from lib_secure_monitoring_service.rov_sms import ROVSMS
from lib_secure_monitoring_service.tests.system_tests.v4_yaml_system_test_runner import V4YamlSystemTestRunner

class V4BaseGraphSystemTester(BaseGraphSystemTester):
    # Placeholders
    GraphInfoCls = "None"
    EngineInputCls = "None"
    base_dir = "None"

    def __init_subclass__(cls, *args, **kwargs):
        """This method essentially creates a list of all subclasses"""

        super().__init_subclass__(*args, **kwargs)
        for attr in ["base_dir",
                     "GraphInfoCls",
                     "EngineInputCls"]:
            assert getattr(cls, attr, None) != "None", attr


    def test_graph(self):
        # Graph data
        peers = self.GraphInfoCls().peer_links
        customer_providers = self.GraphInfoCls().customer_provider_links

        empty_engine_kwargs = {"customer_provider_links": customer_providers,
                               "peer_links": peers,
                               "BaseASCls": self.BaseASCls}

        engine_input_kwargs = {"EngineInputCls": self.EngineInputCls,
                               "attacker_asn": self.attacker_asn,
                               "victim_asn": self.victim_asn,
                               "as_classes": self.as_classes}

        preloaded_engine = None
        preloaded_engine_input = None

        for propagation_round in range(self.propagation_rounds):
            # We need to split dir up so that it can run over many BaseASCls
            dir_ = self.base_dir / (f"{self.BaseASCls.__name__}."
                                    f"{self.AdoptASCls.__name__}")
            dir_ = dir_ / self.propagation_round_str(propagation_round)
            dir_.mkdir(parents=True, exist_ok=True)

            runner = V4YamlSystemTestRunner(
                dir_,
                preloaded_engine=preloaded_engine,
                preloaded_engine_input=preloaded_engine_input,
                debug_fname=self.debug_fname,
                debug_dir=None)

            (preloaded_engine,
             preloaded_engine_input,
             scenario,
             traceback_guess) = runner.run_test(empty_engine_kwargs,
                                                engine_input_kwargs,
                                                propagation_round)

        return preloaded_engine, preloaded_engine_input, traceback_guess

    def test_stable(self):
        (preloaded_engine,
         preloaded_engine_input,
         preloaded_traceback_guess) = self.test_graph()
        preloaded_engine_copy, _, __ = self.test_graph()
        print("Inside test_stable of V4BaseGraphSystemTester")
        scenario = v4_scenario.V4Scenario(engine=preloaded_engine_copy,
                                          engine_input=preloaded_engine_input,
                                          verify_avoid_list=True)
        subgraphs = {"all_ases": set([x.asn for x in preloaded_engine])}

        traceback_guess = scenario.run(subgraphs, 1)

        assert preloaded_engine == preloaded_engine_copy, "Unstable Graph"
        assert preloaded_traceback_guess == traceback_guess, "Unstable Graph"
