from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config140(EngineTestConfig):
    """Attacker Success k=2"""

    name = "140"
    desc = "Subprefix Hijack with V4 Lite k=2"
    graph = graphs.Graph057()
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=3,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        70: ROVSMSK2,
        71: ROVSMSK2,
        72: ROVSMSK2,
        73: ROVSMSK2,
    }
    propagation_rounds = 1
