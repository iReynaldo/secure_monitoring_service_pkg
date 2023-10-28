from typing import Dict, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import EngineTestConfig
from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import ROVSimpleAS
from bgp_simulator_pkg import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import ROVSMSK1


class Config157(EngineTestConfig):
    """Contains config options to run a test
    Tests assume_relays_are_reachable when set to True
    ASN 3 does not have connectivity to relay 12, but with this
    setting it will make it true.
    Note: This test is to show that the check for connectivity is
    bypassed.
    Note: THIS SETTING SHOULD ONLY BE USED WITH PEER RELAY SETTING"""

    name = "157"
    desc = "Direct AutoImmune Attack with ROV++ V4 k=2"
    graph = graphs.Graph061()
    relay_asns = {12, 13}
    scenario = SubprefixAutoImmuneScenario(
        num_attackers=2,
        attacker_asns=graph.attacker_asn_set,
        victim_asns={ASNs.VICTIM.value},
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        relay_asns=relay_asns,
        assume_relays_are_reachable=False,
        indirect=False,
    )

    non_default_as_cls_dict: Dict[int, Type[AS]] = {
        3: ROVSMSK1,
        4: ROVSMSK1,
        8: ROVSMSK1,
        10: ROVSMSK1,
        11: ROVSMSK1,
        7: ROVSimpleAS,
    }
    for asn in relay_asns:
        non_default_as_cls_dict[asn] = ROVSMSK1

    propagation_rounds = 1
