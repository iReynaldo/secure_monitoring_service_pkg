from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import ArtemisSubprefixHijackScenario
from secure_monitoring_service_pkg import Artermis


class Config160(EngineTestConfig):
    """

    """

    name = "160"
    desc = "ARTEMIS Single Attacker"
    graph = graphs.Graph062()
    relay_asns = {12, 13}
    scenario = ArtemisSubprefixHijackScenario(num_attackers=1,
                                              attacker_asns=graph.attacker_asn_set,
                                              victim_asns={ASNs.VICTIM.value},
                                              AdoptASCls=Artermis,
                                              BaseASCls=BGPSimpleAS,
                                              AnnCls=ROVPPAnn,
                                              relay_asns=relay_asns)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: Artermis,
                                                    4: Artermis,
                                                    8: Artermis,
                                                    10: Artermis,
                                                    11: Artermis,
                                                    7: ROVSimpleAS}

    propagation_rounds = 1
