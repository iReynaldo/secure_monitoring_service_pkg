from .disconnected_subgraph import DisconnectedSubgraph
from bgpy import Outcomes
from bgpy import Scenario


class DisconnectedAllSubgraph(DisconnectedSubgraph):
    """A graph for attacker success for etc ASes that adopt"""

    name: str = "v4_disconnected_all"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:
        """Returns the key to be used in shared_data on the subgraph"""

        return f"all_{Outcomes.DISCONNECTED.name}_perc"

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.DISCONNECTED.name
