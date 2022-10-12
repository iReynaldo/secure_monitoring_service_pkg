from typing import Tuple

from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Prefixes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Timestamps

from ..v4_scenario import V4Scenario


class SubprefixAutoImmuneScenario(V4Scenario):

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(SubprefixAutoImmuneScenario, self).__init__(*args, **kwargs)
        self.subprefixes = dict()

    def _get_announcements(self, *args, **kwargs) -> Tuple["Announcement", ...]:
        """Returns victim and attacker anns for autoimmune attack

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

        err: str = "Fix the roa_origins of the " \
                   "announcements for multiple victims"
        assert len(self.victim_asns) == 1, err

        roa_origin: int = next(iter(self.victim_asns))

        engine = kwargs["engine"]
        victim_providers = engine.as_dict[next(iter(self.victim_asns))].providers
        for i, provider in enumerate(victim_providers):
            subprefix = f"1.2.{i}.0/24"
            self.subprefixes[provider.asn] = subprefix
            for attacker_asn in self.attacker_asns:
                anns.append(self.AnnCls(prefix=subprefix,
                                        as_path=(attacker_asn, provider.asn),
                                        timestamp=Timestamps.ATTACKER.value,
                                        seed_asn=attacker_asn,
                                        roa_valid_length=False,
                                        roa_origin=roa_origin,
                                        recv_relationship=Relationships.ORIGIN))

        return tuple(anns)