from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


class Config101(EngineTestConfig):
    """Contains config options to run a test"""

    name = "101"
    desc = "Subprefix Hijack with V4 Lite."
    scenario = V4SubprefixHijackScenario(attacker_asns={ASNs.ATTACKER.value},
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMS,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn)
    graph = graphs.Graph011()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {5: ROVSMS,
                                                    6: ROVSMS,
                                                    1: ROVSMS,
                                                    11: ROVSMS,
                                                    12: ROVSMS}
    propagation_rounds = 1
