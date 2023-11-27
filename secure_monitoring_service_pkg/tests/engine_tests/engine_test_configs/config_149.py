from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_055
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK1

config_149 = EngineTestConfig(
    name="149",
    desc="AutoImmune Attack with V4 Lite k=1",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=2,
        AdoptASCls=ROVSMSK1,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset(graph_055.attacker_asn_set),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            4: ROVSimpleAS,
            70: ROVSMSK1,
            71: ROVSMSK1,
            72: ROVSMSK1,
        }),
    ),
    graph=graph_055,
)
