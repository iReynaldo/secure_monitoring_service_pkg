from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config137(EngineTestConfig):
    """Contains config options to run a test"""

    name = "137"
    desc = "AutoImmune Attack with V4 Lite k=1"
    graph = graphs.Graph054()
    scenario = SubprefixAutoImmuneScenario(num_attackers=2,
                                           attacker_asns=graph.attacker_asn_set,
                                           victim_asns={ASNs.VICTIM.value},
                                           AdoptASCls=ROVSMSK1,
                                           BaseASCls=BGPSimpleAS,
                                           AnnCls=ROVPPAnn)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK1,
                                                    4: ROVSMSK1,
                                                    8: ROVSMSK1,
                                                    10: ROVSMSK1,
                                                    12: ROVSMSK1,
                                                    7: ROVSimpleAS}
    propagation_rounds = 1
