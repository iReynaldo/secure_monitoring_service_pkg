from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import V4SuperprefixPrefixHijack
from secure_monitoring_service_pkg import ROVSMS

class Config166(EngineTestConfig):
    """Contains config options to run a test"""

    name = "166"
    desc = "Superprefix+prefix hijack prefix with V4 Lite"
    scenario = V4SuperprefixPrefixHijack(attacker_asns={ASNs.ATTACKER.value},
                                         victim_asns={ASNs.VICTIM.value},
                                         AdoptASCls=ROVSMS,
                                         BaseASCls=BGPSimpleAS,
                                         AnnCls=ROVPPAnn)
    graph = graphs.Graph045()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMS,
                                                    4: ROVSMS,
                                                    8: ROVSMS,
                                                    10: ROVSMS,
                                                    12: ROVSMS,
                                                    7: ROVSimpleAS}
    propagation_rounds = 1
