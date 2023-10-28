from typing import Tuple

from bgpy import SuperprefixPrefixHijack

from ..v4_scenario import V4Scenario


class V4SuperprefixPrefixHijack(V4Scenario, SuperprefixPrefixHijack):
    def __init__(self, *args, **kwargs):
        super(V4SuperprefixPrefixHijack, self).__init__(*args, **kwargs)
        self.name = "V4SuperprefixPrefixHijackScenario"

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack"""
        anns = super(V4SuperprefixPrefixHijack, self)._get_announcements(
            *args, **kwargs
        )
        anns = anns + tuple(self.generate_relay_announcements())
        return anns
