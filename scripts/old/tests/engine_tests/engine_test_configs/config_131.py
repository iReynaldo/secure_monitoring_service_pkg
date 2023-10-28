from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy.caida_collector import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config131(EngineTestConfig):
    """Contains config options to run a test"""

    name = "131"
    desc = "Subprefix Hijack with V4 Lite k=1"
    scenario = V4SubprefixHijackScenario(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph045()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK1,
        4: ROVSMSK1,
        8: ROVSMSK1,
        10: ROVSMSK1,
        12: ROVSMSK1,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
