from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn
from rovpp import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config106(EngineTestConfig):
    """Contains config options to run a test"""

    name = "106"
    desc = "Subprefix Hijack with V1 Lite."
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1LiteSimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph044()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        1: ROVPPV1LiteSimpleAS,
        8: ROVPPV1LiteSimpleAS,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
