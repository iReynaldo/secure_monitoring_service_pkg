from ..victim_success_subgraph import VictimSuccessSubgraph
from bgp_simulator_pkg.enums import ASTypes
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Scenario


class VictimSuccessAdoptingEtcSubgraph(VictimSuccessSubgraph):
    """A graph for attacker success for etc ASes that adopt"""

    name: str = "v4_victim_success_adopting_etc"

    def _get_subgraph_key(self, scenario: Scenario, *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASTypes.ETC, scenario.AdoptASCls, Outcomes.VICTIM_SUCCESS
        )

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.VICTIM_SUCCESS.name
