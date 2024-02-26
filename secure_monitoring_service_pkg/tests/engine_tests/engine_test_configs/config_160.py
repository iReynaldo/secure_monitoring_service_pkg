from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import ArtemisSubprefixHijackScenario
from secure_monitoring_service_pkg import Artemis


class Config160(EngineTestConfig):
    """

    """

    name = "160"
    desc = "ARTEMIS Single Attacker"
    graph = graphs.Graph069()
    relay_asns = graph.relay_asns
    scenario = ArtemisSubprefixHijackScenario(num_attackers=1,
                                              attacker_asns=graph.attacker_asn_set,
                                              victim_asns={ASNs.VICTIM.value},
                                              AdoptASCls=Artemis,
                                              BaseASCls=BGPSimpleAS,
                                              AnnCls=ROVPPAnn,
                                              relay_asns=relay_asns)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: Artemis,
                                                    4: Artemis,
                                                    8: Artemis,
                                                    10: Artemis,
                                                    11: Artemis,
                                                    7: ROVSimpleAS}

    for relay_asn in relay_asns:
        non_default_as_cls_dict[relay_asn] = Artemis

    propagation_rounds = 1
