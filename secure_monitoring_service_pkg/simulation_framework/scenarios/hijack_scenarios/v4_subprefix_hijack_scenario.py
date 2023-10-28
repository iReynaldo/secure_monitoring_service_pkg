from typing import Tuple

from bgpy import SubprefixHijack

from ..v4_scenario import V4Scenario


class V4SubprefixHijackScenario(V4Scenario, SubprefixHijack):
    def __init__(self, *args, **kwargs):
        super(V4SubprefixHijackScenario, self).__init__(*args, **kwargs)
        self.name = "V4SubprefixHijackScenario"

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack"""
        anns = super(V4SubprefixHijackScenario, self)._get_announcements(
            *args, **kwargs
        )
        anns = anns + tuple(self.generate_relay_announcements())
        return anns
