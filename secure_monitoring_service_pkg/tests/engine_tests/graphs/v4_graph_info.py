from dataclasses import dataclass, field

from bgpy import GraphInfo


@dataclass(frozen=True, slots=True)
class V4GraphInfo(GraphInfo):
    attacker_asn_set: set[int] = field(default_factory=set)
    relays_asns: set[int] = field(default_factory=set)
