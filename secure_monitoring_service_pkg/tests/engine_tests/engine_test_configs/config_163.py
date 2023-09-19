from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config163(EngineTestConfig):
    """

    """

    name = "163"
    desc = "Subprefix Hijack with V4 Lite k=2 " \
           "Relays ARE attacked and Not assumed reachable"
    graph = graphs.Graph063()
    relay_asns = {12, 13}
    scenario = V4SubprefixHijackScenario(num_attackers=2,
                                         attacker_asns=graph.attacker_asn_set,
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMSK2,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn,
                                         relay_asns=relay_asns,
                                         fraction_of_peer_ases_to_attack=1.0,
                                         attack_relays=True,
                                         assume_relays_are_reachable=False)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK2,
                                                    4: ROVSMSK2,
                                                    10: ROVSMSK2,
                                                    11: ROVSMSK2,
                                                    7: ROVSimpleAS}
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK2

    propagation_rounds = 1
