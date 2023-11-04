from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn
from rovpp import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario


class Config100(EngineTestConfig):
    """Contains config options to run a test"""

    name = "100"
    desc = "Subprefix Hijack with V1 Lite."
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVPPV1LiteSimpleAS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph011()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        5: ROVPPV1LiteSimpleAS,
        6: ROVPPV1LiteSimpleAS,
        1: ROVPPV1LiteSimpleAS,
        11: ROVPPV1LiteSimpleAS,
        12: ROVPPV1LiteSimpleAS,
    }
    propagation_rounds = 1
