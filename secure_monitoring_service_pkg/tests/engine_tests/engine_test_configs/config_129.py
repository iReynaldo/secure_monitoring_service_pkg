from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import graphs
from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config129(EngineTestConfig):
    """Contains config options to run a test"""

    name = "129"
    desc = "Subprefix Hijack with V1 Lite"
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1SimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph045()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVPPV1SimpleAS,
        4: ROVPPV1SimpleAS,
        8: ROVPPV1SimpleAS,
        10: ROVPPV1SimpleAS,
        12: ROVPPV1SimpleAS,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
