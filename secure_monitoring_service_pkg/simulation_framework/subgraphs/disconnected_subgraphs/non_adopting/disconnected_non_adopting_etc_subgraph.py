from ..disconnected_subgraph import DisconnectedSubgraph
from bgp_simulator_pkg.enums import ASGroups
from bgp_simulator_pkg import Outcomes


class DisconnectedNonAdoptingEtcSubgraph(DisconnectedSubgraph):
    """A graph for attacker success for etc ASes that don't adopt"""

    name: str = "v4_disconnected_non_adopting_etc"

    def _get_subgraph_key(self, scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASGroups.ETC, scenario.BaseASCls, Outcomes.DISCONNECTED)

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.DISCONNECTED.name
