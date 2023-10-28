from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK2

class Config116(EngineTestConfig):
    """Contains config options to run a test"""

    name = "116"
    desc = "Subprefix Hijack with V4 Lite k=2"
    scenario = V4SubprefixHijackScenario(attacker_asns={ASNs.ATTACKER.value},
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMSK2,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn)
    graph = graphs.Graph046()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {32: ROVSMSK2,
                                                    33: ROVSMSK2,
                                                    77: ROVSimpleAS}
    propagation_rounds = 1
