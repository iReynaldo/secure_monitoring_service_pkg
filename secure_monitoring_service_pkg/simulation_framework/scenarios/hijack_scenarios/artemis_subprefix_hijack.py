from typing import Type, Tuple, Optional

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import SubprefixHijack
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Prefixes

from caida_collector_pkg import AS

from ..v4_scenario import V4Scenario


class ArtemisSubprefixHijackScenario(V4Scenario, SubprefixHijack):
    """
    This Scenario can only be used with the ARTMEIS adopting ASes as adopters.
    Having mixed ROV adoption is acceptable.
    """
    __slots__ = ()

    def __init__(self, *args, relay_asns=None, **kwargs):
        super(ArtemisSubprefixHijackScenario, self).__init__(*args, relay_asns=relay_asns, **kwargs)
        self.name = "ArtemisSubprefixHijackScenario"
        self.relay_prefixes = dict()

    def determine_as_outcome(self,
                             as_obj: AS,
                             ann: Optional[Announcement]
                             ) -> Tuple[Type[Outcomes], Type[int]]:
        """Determines the outcome at an AS

        ann is most_specific_ann is the most specific prefix announcement
        that exists at that AS
        """

        if as_obj.asn in self.attacker_asns:
            return Outcomes.ATTACKER_SUCCESS, as_obj.asn
        elif as_obj.asn in self.victim_asns or as_obj.asn in self.relay_asns:
            return Outcomes.VICTIM_SUCCESS, as_obj.asn
        # End of traceback
        elif (ann is None
              or len(ann.as_path) == 1
              or ann.recv_relationship == Relationships.ORIGIN
              or ann.traceback_end):
            return Outcomes.DISCONNECTED, as_obj.asn
        else:
            return Outcomes.UNDETERMINED, as_obj.asn

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack

        """
        anns = super(ArtemisSubprefixHijackScenario, self)._get_announcements(*args, **kwargs)
        anns = anns + tuple(self.generate_relay_announcements())
        return anns

    def generate_relay_announcements(self):
        anns = list()
        # Setup Relay Announcements
        if self.relay_asns:
            for i, relay_asn in enumerate(self.relay_asns):
                relay_prefix = Prefixes.SUBPREFIX.value
                self.relay_prefixes[relay_asn] = relay_prefix
                anns.append(self.AnnCls(prefix=relay_prefix,
                                        as_path=(relay_asn,),
                                        timestamp=2,
                                        seed_asn=relay_asn,
                                        roa_valid_length=True,
                                        roa_origin=relay_asn,
                                        recv_relationship=Relationships.ORIGIN))
        return anns