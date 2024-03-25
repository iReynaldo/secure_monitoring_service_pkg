from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import RelayPrefixHijack


class Config174(EngineTestConfig):
    """

    """

    name = "174"
    desc = "ROV CDN Prefix Hijack"
    graph = graphs.Graph069()
    relay_asns = graph.relay_asns
    scenario = RelayPrefixHijack(num_attackers=1,
                                  attacker_asns=graph.attacker_asn_set,
                                  victim_asns={ASNs.VICTIM.value},
                                  AdoptASCls=ROVSimpleAS,
                                  BaseASCls=BGPSimpleAS,
                                  AnnCls=ROVPPAnn,
                                  relay_asns=relay_asns)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSimpleAS,
                                                    4: ROVSimpleAS,
                                                    8: ROVSimpleAS,
                                                    10: ROVSimpleAS,
                                                    11: ROVSimpleAS,
                                                    7: ROVSimpleAS}

    for relay_asn in relay_asns:
        non_default_as_cls_dict[relay_asn] = ROVSimpleAS

    propagation_rounds = 1
