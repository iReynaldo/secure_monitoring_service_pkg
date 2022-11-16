from ..disconnected_subgraph import DisconnectedSubgraph
from bgp_simulator_pkg.enums import ASTypes
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Scenario


class DisconnectedAdoptingInputCliqueSubgraph(DisconnectedSubgraph):
    """Graph with attacker success for adopting input clique ASes"""

    name: str = "disconnected_adopting_input_clique"

    def _get_subgraph_key(self,
                          scenario: Scenario,
                          *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(ASTypes.INPUT_CLIQUE,
                                                    scenario.AdoptASCls,
                                                    Outcomes.DISCONNECTED)

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.DISCONNECTED.name
