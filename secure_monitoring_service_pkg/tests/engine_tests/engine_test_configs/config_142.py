from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMS


class Config142(EngineTestConfig):
    """Contains config options to run a test"""

    name = "142"
    desc = "AutoImmune Attackwith V4 Lite"
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=1,
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph043()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMS,
        4: ROVSMS,
        8: ROVSMS,
        10: ROVSMS,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
