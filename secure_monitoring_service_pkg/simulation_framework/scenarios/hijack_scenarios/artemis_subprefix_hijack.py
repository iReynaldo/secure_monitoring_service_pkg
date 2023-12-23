from typing import Type, Tuple, Optional

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import SubprefixHijack
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Prefixes

from caida_collector_pkg import AS

from ..v4_scenario import V4Scenario, RELAY_PREFIX


class ArtemisSubprefixHijackScenario(V4Scenario, SubprefixHijack):
    """
    This Scenario can only be used with the ARTMEIS adopting ASes as adopters.
    Having mixed ROV adoption is acceptable.
    """
    __slots__ = ()

    def __init__(self, fightback_origin_only=False, *args, **kwargs):
        super(ArtemisSubprefixHijackScenario, self).__init__(*args, **kwargs)
        self.name = "ArtemisSubprefixHijackScenario"
        # The following gets updated after traceback of RELAY_PREFIX is done
        self.a_cdn_has_successful_connection_to_origin = False
        self.fightback_origin_only = fightback_origin_only

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
        # Key difference here with the relay_asn as a checkpoint for success
        elif (as_obj.asn in self.victim_asns or
              (self.a_cdn_has_successful_connection_to_origin and as_obj.asn in self.relay_asns)):
            return Outcomes.VICTIM_SUCCESS, as_obj.asn
        # End of traceback
        elif (ann is None
              or len(ann.as_path) == 1
              or ann.recv_relationship == Relationships.ORIGIN
              or ann.traceback_end):
            return Outcomes.DISCONNECTED, as_obj.asn
        else:
            return Outcomes.UNDETERMINED, as_obj.asn

    def get_victim_announcements(self):
        # TODO: This method only works for subprefix hijacks
        #   assuming the victim uses Prefixes.PREFIX.value as origin announcement
        victim_announcements = set()
        for ann in self.announcements:
            for victim_asn in self.victim_asns:
                if victim_asn == ann.as_path[-1] and Prefixes.PREFIX.value == ann.prefix:
                    victim_announcements.add(ann)
        return victim_announcements

    def generate_fightback_relay_announcements(self):
        anns = list()
        relay_asns = set() if not self.relay_asns else self.relay_asns
        # Set of fightback ASes
        fightback_ases = self.victim_asns if self.fightback_origin_only else self.victim_asns | relay_asns
        # Setup Relay Announcements
        for i, asn in enumerate(fightback_ases):
            relay_prefix = Prefixes.SUBPREFIX.value
            self.relay_prefixes[asn] = relay_prefix
            anns.append(self.AnnCls(prefix=relay_prefix,
                                    as_path=(asn,),
                                    timestamp=2,
                                    seed_asn=asn,
                                    roa_valid_length=True,
                                    roa_origin=asn,
                                    recv_relationship=Relationships.ORIGIN))
        return anns

    def generate_origin_relay_announcement(self):
        anns = list()
        # TODO: Extend this for multiple victims if necessary
        victim_asn = next(iter(self.victim_asns))
        anns.append(self.AnnCls(prefix=RELAY_PREFIX,
                                as_path=(victim_asn,),
                                timestamp=2,
                                seed_asn=victim_asn,
                                roa_valid_length=True,
                                roa_origin=victim_asn,
                                recv_relationship=Relationships.ORIGIN))
        if self.attack_relays:
            roa_origin = next(iter(self.victim_asns))
            for attacker_asn in self.attacker_asns:
                anns.append(self.create_attacker_relay_announcement(RELAY_PREFIX, attacker_asn, roa_origin))
        return anns

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack

        """
        anns = super(ArtemisSubprefixHijackScenario, self)._get_announcements(*args, **kwargs)
        # Setup Fightback Announcements
        anns = anns + tuple(self.generate_fightback_relay_announcements())
        # Setup Origin Relay Announcement
        anns = anns + tuple(self.generate_origin_relay_announcement())
        return anns
