from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy.caida_collector import ASNs

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config124(EngineTestConfig):
    """Contains config options to run a test"""

    name = "124"
    desc = "Subprefix Hijack with V4 Lite k=2"
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph042()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        32: ROVSMSK2,
        33: ROVSMSK2,
        77: ROVSimpleAS,
    }
    propagation_rounds = 1
