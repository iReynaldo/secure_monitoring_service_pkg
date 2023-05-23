from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK1
from secure_monitoring_service_pkg import CDN


class Config165(EngineTestConfig):
    """

    """

    name = "165"
    desc = "Subprefix Hijack with V4 Lite k=1" \
           "Relays NOT attacked and Not assumed reachable\n" \
           "CDN Neustar being used"
    graph = graphs.Graph065()
    relay_asns = CDN().neustar
    scenario = V4SubprefixHijackScenario(num_attackers=1,
                                         attacker_asns=graph.attacker_asn_set,
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMSK1,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn,
                                         relay_asns=relay_asns,
                                         attack_relays=False,
                                         assume_relays_are_reachable=False)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {1: ROVSMSK1,
                                                    4: ROVSMSK1}
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK1

    propagation_rounds = 1
