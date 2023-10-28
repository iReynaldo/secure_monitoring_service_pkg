from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config100(EngineTestConfig):
    """Contains config options to run a test"""

    name = "100"
    desc = "Subprefix Hijack with V1 Lite."
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1LiteSimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph011()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        5: ROVPPV1LiteSimpleAS,
        6: ROVPPV1LiteSimpleAS,
        1: ROVPPV1LiteSimpleAS,
        11: ROVPPV1LiteSimpleAS,
        12: ROVPPV1LiteSimpleAS,
    }
    propagation_rounds = 1
