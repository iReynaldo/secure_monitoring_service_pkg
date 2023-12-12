from frozendict import frozendict

from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK2

# Set Relay ASes and AS Policy Classes
relay_asns = {12, 13}
non_default_as_cls_dict = {
    3: ROVSMSK2,
    4: ROVSMSK2,
    10: ROVSMSK2,
    11: ROVSMSK2,
    7: ROVSimpleAS,
}
for asn in relay_asns:
    non_default_as_cls_dict[asn] = ROVSMSK2

# Create Config
config_162 = EngineTestConfig(
    name="162",
    desc="Subprefix Hijack with V4 Lite k=2 "
         "Relays Not attacked and Not assumed reachable",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        num_attackers=2,
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset(graphs.Graph063().attacker_asn_set),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(non_default_as_cls_dict),
        attack_relays=False,
        assume_relays_are_reachable=False,
    ),
    graph=graphs.Graph063(),
    relay_asns=relay_asns,
    propagation_rounds=1,
)
