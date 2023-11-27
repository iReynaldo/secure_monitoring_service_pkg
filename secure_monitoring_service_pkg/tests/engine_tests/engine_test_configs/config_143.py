from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_043
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK1

config_143 = EngineTestConfig(
    name="143",
    desc="AutoImmune Attack with V4 Lite k=1",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=1,
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            3: ROVSMSK1,
            4: ROVSMSK1,
            8: ROVSMSK1,
            10: ROVSMSK1,
            7: ROVSimpleAS,
        }),
    ),
    graph=graph_043,
)
