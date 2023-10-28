from .attacker_success_subgraph import AttackerSuccessSubgraph
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Scenario


class AttackerSuccessAllSubgraph(AttackerSuccessSubgraph):
    """A graph for attacker success for etc ASes that adopt"""

    name: str = "v4_attacker_success_all"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:
        """Returns the key to be used in shared_data on the subgraph"""

        return f"all_{Outcomes.ATTACKER_SUCCESS.name}_perc"

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.ATTACKER_SUCCESS.name
