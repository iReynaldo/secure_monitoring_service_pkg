from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy.caida_collector import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config164(EngineTestConfig):
    """ """

    name = "164"
    desc = (
        "Subprefix Hijack with V4 Lite k=1"
        "Relays NOT attacked and Not assumed reachable\n"
        "No CDN used (i.e. Peer like setting)"
    )

    graph = graphs.Graph064()
    relay_asns = {2, 3, 6}
    scenario = V4SubprefixHijackScenario(
        num_attackers=1,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
        attack_relays=False,
        assume_relays_are_reachable=False,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {1: ROVSMSK1, 4: ROVSMSK1}
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK1

    propagation_rounds = 1
