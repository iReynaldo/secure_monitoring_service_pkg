from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_043
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK2

config_144 = EngineTestConfig(
    name="144",
    desc="AutoImmune Attack with V4 Lite k=2",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=1,
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            3: ROVSMSK2,
            4: ROVSMSK2,
            8: ROVSMSK2,
            10: ROVSMSK2,
            7: ROVSimpleAS,
        }),
    ),
    graph=graph_043,
)
