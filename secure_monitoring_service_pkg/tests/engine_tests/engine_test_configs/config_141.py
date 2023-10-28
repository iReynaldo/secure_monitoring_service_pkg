from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config141(EngineTestConfig):
    """Attacker Fail k=2"""

    name = "141"
    desc = "AutoImmune Attack with V4 Lite k=2"
    graph = graphs.Graph058()
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=2,
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
