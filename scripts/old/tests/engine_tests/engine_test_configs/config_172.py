from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy.caida_collector import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS
from secure_monitoring_service_pkg import CDN


class Config172(EngineTestConfig):
    """ """

    name = "172"
    desc = (
        "Subprefix Hijack with V4 k=0 \n"
        "CDN Setting (Akamai) \n"
        "Relays ARE attacked and Not assumed reachable \n"
        "Tunneling Others Traffic is enabled"
    )
    graph = graphs.Graph068()
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
        tunnel_customers_traffic=True,
        assume_relays_are_reachable=False,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMS}
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMS

    propagation_rounds = 1
