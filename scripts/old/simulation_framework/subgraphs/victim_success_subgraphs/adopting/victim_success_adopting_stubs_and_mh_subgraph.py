from ..victim_success_subgraph import VictimSuccessSubgraph
from bgpy.enums import ASTypes
from bgpy import Outcomes


class VictimSuccessAdoptingStubsAndMHSubgraph(VictimSuccessSubgraph):
    """Graph for attacker success with adopting stubs or multihomed ASes"""

    name: str = "v4_victim_success_adopting_stubs_and_multihomed"

    def _get_subgraph_key(self, scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.STUBS_OR_MH, scenario.AdoptASCls, Outcomes.VICTIM_SUCCESS
        )

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.VICTIM_SUCCESS.name
