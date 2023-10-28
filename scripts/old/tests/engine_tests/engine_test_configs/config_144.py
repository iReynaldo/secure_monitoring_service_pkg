from typing import Dict, Type

from bgpy import AS

from bgpy import graphs
from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config144(EngineTestConfig):
    """Contains config options to run a test"""

    name = "144"
    desc = "AutoImmune Attack with V4 Lite k=2"
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=1,
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )
    graph = graphs.Graph043()
    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK2,
        4: ROVSMSK2,
        8: ROVSMSK2,
        10: ROVSMSK2,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
