from typing import Dict, Type

from bgpy import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config125(EngineTestConfig):
    """Contains config options to run a test"""

    name = "125"
    desc = "Subprefix Hijack with V1 Lite"
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1SimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph043()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVPPV1SimpleAS,
        4: ROVPPV1SimpleAS,
        8: ROVPPV1SimpleAS,
        10: ROVPPV1SimpleAS,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
