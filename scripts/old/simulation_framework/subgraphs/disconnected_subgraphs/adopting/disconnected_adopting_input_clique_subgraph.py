from ..disconnected_subgraph import DisconnectedSubgraph
from bgpy.enums import ASTypes
from bgpy import Outcomes
from bgpy import Scenario


class DisconnectedAdoptingInputCliqueSubgraph(DisconnectedSubgraph):
    """Graph with attacker success for adopting input clique ASes"""

    name: str = "v4_disconnected_adopting_input_clique"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.INPUT_CLIQUE, scenario.AdoptASCls, Outcomes.DISCONNECTED
        )

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.DISCONNECTED.name
