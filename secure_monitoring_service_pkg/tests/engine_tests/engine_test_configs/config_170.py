from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVPPO
from secure_monitoring_service_pkg import CDN


class Config170(EngineTestConfig):
    """

    """

    name = "170"
    desc = "Subprefix Hijack with ROV++ V1 Lite Overlayed\n" \
           "Relays NOT attacked and Not assumed reachable\n" \
           "CDN Neustar being used"
    graph = graphs.Graph065()
    relay_asns = CDN().neustar
    scenario = V4SubprefixHijackScenario(num_attackers=1,
                                         attacker_asns=graph.attacker_asn_set,
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVPPO,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn,
                                         relay_asns=relay_asns,
                                         probe_data_plane=False,
                                         attack_relays=False,
                                         assume_relays_are_reachable=False)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {1: ROVPPO,
                                                    4: ROVPPO}
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVPPO

    propagation_rounds = 1
