from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import SimulationEngine
from typing import Any, Dict

from ...v4_subgraph import V4Subgraph

class AvoidListAccuracySubgraph(V4Subgraph):
    """A graph to check the accuracy of the avoid list
    (i.e. how many ASes on the avoid list are incorrectly on the avoid list.)"""

    name: str = "avoid_list_accuracy"

    def _add_traceback_to_shared_data(self,
                                      shared: Dict[Any, Any],
                                      engine: SimulationEngine,
                                      scenario: Scenario,
                                      outcomes):
        """Adds traceback info to shared data"""

        # ------------------------------------------------------------------

        if ("size_of_avoid_list" not in shared) or (shared["size_of_avoid_list"] == 0):
            shared["avoid_list_accuracy"] = 1
        else:
            shared["avoid_list_accuracy"] = (shared["num_ases_should_not_be_on_avoid_list"] - shared["size_of_avoid_list"]) / shared["size_of_avoid_list"]
        # ------------------------------------------------------------------
        return super()._add_traceback_to_shared_data(
            shared, engine, scenario, outcomes)

    def _get_subgraph_key(self,
                          scenario: Scenario,
                          *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return f"avoid_list_accuracy" # noqa E509

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return "Percent of inaccurate ASNs in Avoid List"