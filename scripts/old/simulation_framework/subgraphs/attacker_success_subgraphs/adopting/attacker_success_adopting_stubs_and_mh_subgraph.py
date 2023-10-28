from bgp_simulator_pkg.enums import ASTypes
from bgp_simulator_pkg import Outcomes

from ..attacker_success_subgraph import AttackerSuccessSubgraph


class AttackerSuccessAdoptingStubsAndMHSubgraph(AttackerSuccessSubgraph):
    """Graph for attacker success with adopting stubs or multihomed ASes"""

    name: str = "v4_attacker_success_adopting_stubs_and_multihomed"

    def _get_subgraph_key(self, scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.STUBS_OR_MH, scenario.AdoptASCls, Outcomes.ATTACKER_SUCCESS
        )

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.ATTACKER_SUCCESS.name
