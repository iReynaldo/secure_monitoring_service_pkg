from typing import Type, Tuple, Optional

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import PrefixHijack
from bgp_simulator_pkg import Prefixes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Timestamps
from caida_collector_pkg import AS

from .artemis_subprefix_hijack import ArtemisSubprefixHijackScenario
from ..v4_scenario import V4Scenario


class RelayPrefixHijack(V4Scenario, PrefixHijack):
    """
    Designed to test how influential the CDNs are compared to the attacker
    """
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(RelayPrefixHijack, self).__init__(*args, **kwargs)
        self.name = "RelayPrefixHijack"
        self.attacker_victim_asns_preset = True
        self.victim_asns = self.relay_asns
        self.num_victims = len(self.relay_asns)
        self.relay_asns = None

    def _get_announcements(self,
                           *args,
                           **kwargs
                           ) -> Tuple["Announcement", ...]:
        """Returns the two announcements seeded for this engine input

        This engine input is for a prefix hijack,
        consisting of a valid prefix and invalid prefix

        for subclasses of this EngineInput, you can set AnnCls equal to
        something other than Announcement
        """

        anns = list()
        for victim_asn in self.victim_asns:
            anns.append(self.AnnCls(prefix=Prefixes.PREFIX.value,
                                    as_path=(victim_asn,),
                                    timestamp=Timestamps.VICTIM.value,
                                    seed_asn=victim_asn,
                                    roa_valid_length=True,
                                    roa_origin=victim_asn,
                                    recv_relationship=Relationships.ORIGIN))

        roa_origin: int = next(iter(self.victim_asns))

        for attacker_asn in self.attacker_asns:
            anns.append(self.AnnCls(prefix=Prefixes.PREFIX.value,
                                    as_path=(attacker_asn,),
                                    timestamp=Timestamps.ATTACKER.value,
                                    seed_asn=attacker_asn,
                                    roa_valid_length=True,
                                    roa_origin=roa_origin,
                                    recv_relationship=Relationships.ORIGIN))

        return tuple(anns)

    def _set_attackers_victims(self, *args, **kwargs):
        """Sets attacker victim pair"""

        self.attacker_asns = self._get_attacker_asns(*args, **kwargs)

        # Only run if attacker and victims aren't already set
        if not self.attacker_victim_asns_preset:
            self.victim_asns = self._get_victim_asns(*args, **kwargs)


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
        elif as_obj.asn in self.victim_asns:
            return Outcomes.VICTIM_SUCCESS, as_obj.asn
        # End of traceback
        elif (ann is None
              or len(ann.as_path) == 1
              or ann.recv_relationship == Relationships.ORIGIN
              or ann.traceback_end):
            return Outcomes.DISCONNECTED, as_obj.asn
        else:
            return Outcomes.UNDETERMINED, as_obj.asn

