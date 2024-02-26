from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


class Config179(EngineTestConfig):
    """

    """

    name = "179"
    desc = "Subprefix Hijack, Minerva Receiver-Based"
    graph = graphs.Graph073()
    relay_asns = graph.relay_asns
    scenario = V4SubprefixHijackScenario(num_attackers=1,
                                         attacker_asns=graph.attacker_asn_set,
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMS,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn,
                                         relay_asns=relay_asns,
                                         attack_relays=True)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {7: ROVSMS,
                                                    8: ROVSMS}

    for relay_asn in relay_asns:
        non_default_as_cls_dict[relay_asn] = ROVSMS

    propagation_rounds = 1
