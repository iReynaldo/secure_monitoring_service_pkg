from lib_bgp_simulator.tests.utils.yaml_system_test_runner import YamlSystemTestRunner
from lib_bgp_simulator.simulator.data_point import DataPoint

from secure_monitoring_service_pkg.simulation_framework.v4_subprefix_hijack_scenario import V4SubprefixHijackScenario

class V4YamlSystemTestRunner(YamlSystemTestRunner):

    def get_results(self,
                    engine,
                    engine_input,
                    BaseASCls,
                    propagation_round,
                    preloaded=False):
        if not preloaded:
            engine.setup(engine_input, BaseASCls, None)

        scenario = V4SubprefixHijackScenario(engine=engine, engine_input=engine_input, verify_avoid_list=True)
        subgraphs = {"all_ases": set([x.asn for x in engine])}

        # 0 for the propagation round. Change this later
        traceback_guess = scenario.run(subgraphs, propagation_round)

        # Run post propagation hooks for policies that have them
        dp = DataPoint(None, None, propagation_round)
        engine_input.post_propagation_hook(engine, dp)
        return scenario, traceback_guess