from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy.caida_collector import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS
from secure_monitoring_service_pkg import CDN


class Config171(EngineTestConfig):
    """ """

    name = "171"
    desc = (
        "Subprefix Hijack with V4 k=0 \n"
        "CDN Setting (Akamai) \n"
        "Relays ARE attacked and Not assumed reachable"
    )
    graph = graphs.Graph067()
    relay_asns = CDN.akamai
    scenario = V4SubprefixHijackScenario(
        num_attackers=1,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
        fraction_of_peer_ases_to_attack=1.0,
        attack_relays=True,
        assume_relays_are_reachable=False,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMS,
        4: ROVSMS,
        10: ROVSMS,
        11: ROVSMS,
        7: ROVSimpleAS,
    }
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMS

    propagation_rounds = 1
