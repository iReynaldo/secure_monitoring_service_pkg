from bgp_simulator_pkg.enums import ASTypes
from bgp_simulator_pkg import Outcomes

from ..attacker_success_subgraph import AttackerSuccessSubgraph

class AttackerSuccessNonAdoptingEtcSubgraph(AttackerSuccessSubgraph):
    """A graph for attacker success for etc ASes that don't adopt"""

    name: str = "attacker_success_non_adopting_etc_v4"

    def _get_subgraph_key(self, scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.ETC, scenario.BaseASCls, Outcomes.ATTACKER_SUCCESS)

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.ATTACKER_SUCCESS.name
