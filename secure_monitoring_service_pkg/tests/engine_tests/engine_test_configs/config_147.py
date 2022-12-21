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


class Config147(EngineTestConfig):
    """Contains config options to run a test"""

    name = "147"
    desc = "AutoImmune Attack with V4 Lite K=2"
    graph = graphs.Graph059()
    scenario = SubprefixAutoImmuneScenario(num_attackers=2,
                                           attacker_asns=graph.attacker_asn_set,
                                           victim_asns={ASNs.VICTIM.value},
                                           AdoptASCls=ROVSMSK2,
                                           BaseASCls=BGPSimpleAS,
                                           AnnCls=ROVPPAnn)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK2,
                                                    4: ROVSMSK2,
                                                    8: ROVSMSK2,
                                                    10: ROVSMSK2,
                                                    11: ROVSMSK2,
                                                    7: ROVSimpleAS}
    propagation_rounds = 1
