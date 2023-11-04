from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


class Config104(EngineTestConfig):
    """Contains config options to run a test"""

    name = "104"
    desc = "Subprefix Hijack with V4 Lite."
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph027()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        4: ROVSMS,
        10: ROVSMS,
        ASNs.VICTIM.value: ROVSMS,
    }
    propagation_rounds = 1
