from bgp_simulator_pkg import SubprefixHijack

from ..v4_scenario import V4Scenario


class V4SubprefixHijackScenario(V4Scenario, SubprefixHijack):

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(V4SubprefixHijackScenario, self).__init__(*args, **kwargs)
        self.name = "V4SubprefixHijackScenario"