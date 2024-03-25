from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4OriginHijack
from secure_monitoring_service_pkg import ROVSMS


class Config177(EngineTestConfig):
    """

    """

    name = "177"
    desc = "Origin Hijack, Minerva Sender-Based"
    graph = graphs.Graph071()
    relay_asns = graph.relay_asns
    scenario = V4OriginHijack(num_attackers=1,
                              attacker_asns=graph.attacker_asn_set,
                              victim_asns={ASNs.VICTIM.value},
                              AdoptASCls=ROVSMS,
                              BaseASCls=BGPSimpleAS,
                              AnnCls=ROVPPAnn,
                              relay_asns=relay_asns)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMS,
                                                    4: ROVSMS,
                                                    8: ROVSMS,
                                                    10: ROVSMS,
                                                    11: ROVSMS,
                                                    7: ROVSimpleAS}

    for relay_asn in relay_asns:
        non_default_as_cls_dict[relay_asn] = ROVSMS

    propagation_rounds = 1
