from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


class Config104(EngineTestConfig):
    """Contains config options to run a test"""

    name = "104"
    desc = "Subprefix Hijack with V4 Lite."
    scenario = V4SubprefixHijackScenario(attacker_asns={ASNs.ATTACKER.value},
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMS,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn)
    graph = graphs.Graph027()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {4: ROVSMS,
                                                    10: ROVSMS,
                                                    ASNs.VICTIM.value: ROVSMS}
    propagation_rounds = 1
