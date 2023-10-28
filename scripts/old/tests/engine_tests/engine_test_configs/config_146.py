from typing import Dict, Type

from bgpy import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp_pkg import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config146(EngineTestConfig):
    """Contains config options to run a test"""

    name = "146"
    desc = "AutoImmune Attack with V4 Lite K=1"
    graph = graphs.Graph059()
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK1,
        4: ROVSMSK1,
        8: ROVSMSK1,
        10: ROVSMSK1,
        11: ROVSMSK1,
        7: ROVSimpleAS,
    }
    propagation_rounds = 1
