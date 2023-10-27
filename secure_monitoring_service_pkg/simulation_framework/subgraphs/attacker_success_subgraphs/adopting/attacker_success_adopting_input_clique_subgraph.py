from bgp_simulator_pkg.enums import ASTypes
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Scenario

from ..attacker_success_subgraph import AttackerSuccessSubgraph


class AttackerSuccessAdoptingInputCliqueSubgraph(AttackerSuccessSubgraph):
    """Graph with attacker success for adopting input clique ASes"""

    name: str = "v4_attacker_success_adopting_input_clique"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.INPUT_CLIQUE, scenario.AdoptASCls, Outcomes.ATTACKER_SUCCESS
        )

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.ATTACKER_SUCCESS.name
