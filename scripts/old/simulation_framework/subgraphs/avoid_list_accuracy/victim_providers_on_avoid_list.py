from bgpy import Scenario
from bgpy import SimulationEngine
from typing import Any, Dict

from secure_monitoring_service_pkg.simulation_framework.subgraphs.v4_subgraph import (
    V4Subgraph,
)


class VictimProvidersOnAvoidList(V4Subgraph):
    """A graph to check the fraction of victim providers on the avoid list"""

    name: str = "victim_providers_on_avoid_list"

    def _add_traceback_to_shared_data(
        self,
        shared: Dict[Any, Any],
        engine: SimulationEngine,
        scenario: Scenario,
        outcomes,
    ):
        """Adds traceback info to shared data"""

        # ------------------------------------------------------------------
        if ("num_of_victim_providers" not in shared) or (
            shared["num_of_victim_providers"] == 0
        ):
            shared["victim_providers_on_avoid_list"] = 0
        else:
            shared["victim_providers_on_avoid_list"] = (
                shared["num_victim_providers_on_avoid_list"]
                / shared["num_of_victim_providers"]
            )
        # ------------------------------------------------------------------
        return super()._add_traceback_to_shared_data(shared, engine, scenario, outcomes)

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return f"victim_providers_on_avoid_list"  # noqa E509

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return "Percent of Victim's Provider ASNs are on the Avoid List"
