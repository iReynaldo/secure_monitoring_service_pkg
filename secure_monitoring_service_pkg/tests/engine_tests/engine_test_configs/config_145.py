from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK3


class Config145(EngineTestConfig):
    """Contains config options to run a test"""

    name = "145"
    desc = "AutoImmune Attack with V4 Lite"
    graph = graphs.Graph059()
    scenario = SubprefixAutoImmuneScenario(num_attackers=2,
                                           attacker_asns=graph.attacker_asn_set,
                                           victim_asns={ASNs.VICTIM.value},
                                           AdoptASCls=ROVSMSK3,
                                           BaseASCls=BGPSimpleAS,
                                           AnnCls=ROVPPAnn)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK3,
                                                    4: ROVSMSK3,
                                                    8: ROVSMSK3,
                                                    10: ROVSMSK3,
                                                    11: ROVSMSK3,
                                                    7: ROVSimpleAS}
    propagation_rounds = 1
