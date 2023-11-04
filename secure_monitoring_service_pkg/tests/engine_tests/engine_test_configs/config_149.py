from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config149(EngineTestConfig):
    """Attacker Success k=1"""

    name = "149"
    desc = "AutoImmune Attack with V4 Lite k=1"
    graph = graphs.Graph055()
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        4: ROVSimpleAS,
        70: ROVSMSK1,
        71: ROVSMSK1,
        72: ROVSMSK1,
    }
    propagation_rounds = 1
