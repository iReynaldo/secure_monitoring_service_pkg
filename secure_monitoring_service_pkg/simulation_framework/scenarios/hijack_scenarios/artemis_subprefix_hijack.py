from typing import Type, Tuple, Optional

from bgpy import Announcement
from bgpy import Relationships
from bgpy import SubprefixHijack
from bgpy import Outcomes
from bgpy import Prefixes

from bgpy import AS

from ..v4_scenario import V4Scenario


class ArtemisSubprefixHijackScenario(V4Scenario, SubprefixHijack):
    """
    This Scenario can only be used with the ARTMEIS adopting ASes as adopters.
    Having mixed ROV adoption is acceptable.
    """

    def __init__(self, *args, relay_asns=None, **kwargs):

        self.relay_prefixes = dict()
        super(ArtemisSubprefixHijackScenario, self).__init__(
            *args, relay_asns=relay_asns, **kwargs
        )
        self.name = "ArtemisSubprefixHijackScenario"


    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack"""
        anns = super(ArtemisSubprefixHijackScenario, self)._get_announcements(
            *args, **kwargs
        )
        anns = anns + tuple(self.generate_relay_announcements())
        return anns

    def generate_relay_announcements(self):
        anns = list()
        # Setup Relay Announcements
        if self.scenario_config.relay_asns:
            for i, relay_asn in enumerate(self.scenario_config.relay_asns):
                relay_prefix = Prefixes.SUBPREFIX.value
                self.relay_prefixes[relay_asn] = relay_prefix
                anns.append(
                    self.scenario_config.AnnCls(
                        prefix=relay_prefix,
                        as_path=(relay_asn,),
                        timestamp=2,
                        seed_asn=relay_asn,
                        roa_valid_length=True,
                        roa_origin=relay_asn,
                        recv_relationship=Relationships.ORIGIN,
                    )
                )
        return anns
