from bgpy.enums import ASGroups
from bgpy import Outcomes
from bgpy import Scenario

from ..attacker_success_subgraph import AttackerSuccessSubgraph

class AttackerSuccessAdoptingEtcSubgraph(AttackerSuccessSubgraph):
    """A graph for attacker success for etc ASes that adopt"""

    name: str = "v4_attacker_success_adopting_etc"

    def _get_subgraph_key(self,
                          scenario: Scenario,
                          *args) -> str:  # type: ignore
        """Returns the key to be used in shared_data on the subgraph"""

        return self._get_as_type_pol_outcome_perc_k(
            ASGroups.ETC, scenario.scenario_config.AdoptASCls, Outcomes.ATTACKER_SUCCESS)

    @property
    def y_axis_label(self) -> str:
        """returns y axis label"""

        return Outcomes.ATTACKER_SUCCESS.name
