from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK2

class Config136(EngineTestConfig):
    """Contains config options to run a test"""

    name = "136"
    desc = "Subprefix Hijack with V4 Lite k=2"
    scenario = SubprefixAutoImmuneScenario(attacker_asns={ASNs.ATTACKER.value},
                                           victim_asns={ASNs.VICTIM.value},
                                           AdoptASCls=ROVSMSK2,
                                           BaseASCls=BGPSimpleAS,
                                           AnnCls=ROVPPAnn)
    graph = graphs.Graph053()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK2,
                                                    4: ROVSMSK2,
                                                    8: ROVSMSK2,
                                                    10: ROVSMSK2,
                                                    12: ROVSMSK2,
                                                    7: ROVSimpleAS}
    propagation_rounds = 1
