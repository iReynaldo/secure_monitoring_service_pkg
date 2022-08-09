from collections import defaultdict
from copy import deepcopy

from lib_bgp_simulator.simulator.graph.graph import Graph
from lib_bgp_simulator.simulator.data_point import DataPoint

from lib_secure_monitoring_service.v4_scenario import V4Scenario
from lib_secure_monitoring_service import metadata_collector

class V4Graph(Graph):

    def __init__(self, *args, verify_avoid_list=False, **kwargs):
        super(V4Graph, self).__init__(*args, **kwargs)
        self.verify_avoid_list_flag = verify_avoid_list

    def _run_chunk(self, percent_adopt_trials):
        # Engine is not picklable or dillable AT ALL, so do it here
        # Changing recursion depth does nothing
        # Making nothing a reference does nothing
        engine = self._get_engine_and_save_subgraphs()

        data_points = defaultdict(list)

        for percent_adopt, trial in percent_adopt_trials:
            og_engine_input = self.EngineInputCls(self.subgraphs,
                                                  engine,
                                                  percent_adopt)
            for ASCls in self.adopt_as_classes:
                print(f"{percent_adopt}% {ASCls.name}, #{trial}",
                      end = "                             " + "\r")
                metadata_collector.cur_percent_adoption = percent_adopt
                metadata_collector.cur_trial = trial
                # --------------------------------------------------
                # Deepcopy input to make sure input is fresh
                engine_input = deepcopy(og_engine_input)
                # Change AS Classes, seed announcements before propagation
                engine.setup(engine_input, self.BaseASCls, ASCls)

                for propagation_round in range(self.propagation_rounds):
                    # Generate the test
                    scenario = V4Scenario(trial=trial,
                                          engine=engine,
                                          engine_input=engine_input,
                                          profiler=self.profiler,
                                          verify_avoid_list=self.verify_avoid_list_flag)
                    # Run test, remove reference to engine and return it
                    scenario.run(self.subgraphs, propagation_round)
                    # Get data point - just a frozen data class
                    # Just makes it easier to access properties later
                    dp = DataPoint(percent_adopt, ASCls, propagation_round)
                    # Append the test to all tests for that data point
                    data_points[dp].append(scenario)
                    engine_input.post_propagation_hook(engine, dp)
        return data_points