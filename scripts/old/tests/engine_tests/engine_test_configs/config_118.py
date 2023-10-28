from typing import Dict, Type

from bgpy import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


class Config118(EngineTestConfig):
    """Contains config options to run a test"""

    name = "118"
    desc = "Subprefix Hijack with V4 Lite"
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph041()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        32: ROVSMS,
        33: ROVSMS,
        55: ROVSMS,
        77: ROVSimpleAS,
    }
    propagation_rounds = 1
