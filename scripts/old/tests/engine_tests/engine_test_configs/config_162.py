from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy.caida_collector import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config162(EngineTestConfig):
    """ """

    name = "162"
    desc = (
        "Subprefix Hijack with V4 Lite k=2 "
        "Relays Not attacked and Not assumed reachable"
    )
    graph = graphs.Graph063()
    relay_asns = {12, 13}
    scenario = V4SubprefixHijackScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
        attack_relays=False,
        assume_relays_are_reachable=False,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK2,
        4: ROVSMSK2,
        10: ROVSMSK2,
        11: ROVSMSK2,
        7: ROVSimpleAS,
    }
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK2

    propagation_rounds = 1
