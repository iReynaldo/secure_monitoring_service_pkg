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


class Config168(EngineTestConfig):
    """Contains config options to run a test
    This is a Direct AutoImmune attack. """

    name = "168"
    desc = "Direct AutoImmune Attack with ROV++ V4 k=1\nThe origin has two providers" \
           "\nASes 3, 8, 11, and 7 are adopters" \
           "\nAS 7 is adopting ROV" \
           "\nOrigin 777 has two providers ASes 1 and 14" \
           "\nThe adopting ASes get disconnected because k < m"
    graph = graphs.Graph066()
    scenario = SubprefixAutoImmuneScenario(num_attackers=2,
                                           attacker_asns=graph.attacker_asn_set,
                                           victim_asns={ASNs.VICTIM.value},
                                           AdoptASCls=ROVSMSK1,
                                           BaseASCls=BGPSimpleAS,
                                           AnnCls=ROVPPAnn,
                                           assume_relays_are_reachable=True,
                                           indirect=False)

    non_default_as_cls_dict: Dict[int, Type[AS]] = {3: ROVSMSK1,
                                                    8: ROVSMSK1,
                                                    11: ROVSMSK1,
                                                    7: ROVSimpleAS}

    propagation_rounds = 1
