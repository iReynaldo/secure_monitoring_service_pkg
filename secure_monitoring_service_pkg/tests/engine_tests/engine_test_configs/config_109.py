from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn
from rovpp import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config109(EngineTestConfig):
    """Contains config options to run a test"""

    name = "109"
    desc = "Subprefix Hijack with V1 Lite."
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1LiteSimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph020()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        32: ROVPPV1LiteSimpleAS,
        33: ROVPPV1LiteSimpleAS,
        89: ROVPPV1LiteSimpleAS,
        77: ROVSimpleAS,
    }
    propagation_rounds = 1
