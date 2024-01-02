from typing import Tuple, Set, Dict, Optional, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Prefixes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Timestamps

from ..v4_scenario import V4Scenario
from ....simulation_engine.report import Report

from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger
from ....simulation_engine import ROVSMS


class V4OriginHijack(V4Scenario):

    def __init__(self, *args, relay_asns=None, **kwargs):
        super(V4OriginHijack, self).__init__(*args, relay_asns=relay_asns, **kwargs)
        self.name = "V4OriginHijack"

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim, attacker, and relay anns for autoimmune attack

        """

        anns = list()
        # Setup Victim Announcements
        for victim_asn in self.victim_asns:
            anns.append(self.AnnCls(prefix=Prefixes.PREFIX.value,
                                    as_path=(victim_asn,),
                                    timestamp=Timestamps.VICTIM.value,
                                    seed_asn=victim_asn,
                                    roa_valid_length=True,
                                    roa_origin=victim_asn,
                                    recv_relationship=Relationships.ORIGIN))

        err: str = "Fix the roa_origins of the " \
                   "announcements for multiple victims"
        assert len(self.victim_asns) == 1, err

        roa_origin: int = next(iter(self.victim_asns))

        for attacker_asn in self.attacker_asns:
            anns.append(self.AnnCls(prefix=Prefixes.PREFIX.value,
                                    as_path=(attacker_asn, roa_origin),
                                    timestamp=Timestamps.ATTACKER.value,
                                    seed_asn=attacker_asn,
                                    roa_valid_length=True,
                                    roa_origin=roa_origin,
                                    recv_relationship=Relationships.ORIGIN))

        anns = tuple(anns) + tuple(self.generate_relay_announcements())
        return anns
