from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_011
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs
from bgpy.simulation_framework import ScenarioConfig

from rovpp import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario



config_103 = EngineTestConfig(
    name="config_103",
    desc="Subprefix Hijack with V1 Lite.",
    scenario_config=ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AdoptASCls=ROVPPV1LiteSimpleAS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            4: ROVPPV1LiteSimpleAS,
            10: ROVPPV1LiteSimpleAS,
            ASNs.VICTIM.value: ROVPPV1LiteSimpleAS,
        }),
    ),
    graph=graph_011,
)