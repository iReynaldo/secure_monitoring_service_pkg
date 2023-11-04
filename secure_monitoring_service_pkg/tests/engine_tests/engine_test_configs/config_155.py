from typing import Dict, Type

from bgpy.caida_collector import AS

from bgpy import EngineTestConfig
from bgpy import BGPSimpleAS
from bgpy import ROVSimpleAS
from bgpy import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK2


class Config155(EngineTestConfig):
    """Contains config options to run a test
    Tests assume_relays_are_reachable when set to True
    ASN 3 does not have connectivity to relay 12, but with this
    setting it will make it true.
    Note: This test is to show that the check for connectivity is
    bypassed.
    Note: THIS SETTING SHOULD ONLY BE USED WITH PEER RELAY SETTING"""

    name = "155"
    desc = "AutoImmune Attack with ROV++ V4 k=2"
    graph = graphs.Graph061()
    relay_asns = {12, 13}
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
        assume_relays_are_reachable=True,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK2,
        4: ROVSMSK2,
        8: ROVSMSK2,
        10: ROVSMSK2,
        11: ROVSMSK2,
        7: ROVSimpleAS,
    }
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK2
    propagation_rounds = 1
