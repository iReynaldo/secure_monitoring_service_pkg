from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_011
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs
from bgpy.simulation_framework import ScenarioConfig

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS


config_101 = EngineTestConfig(
    name="config_101",
    desc="Subprefix Hijack with V4 Lite.",
    scenario_config=ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AdoptASCls=ROVSMS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            5: ROVSMS,
            6: ROVSMS,
            1: ROVSMS,
            11: ROVSMS,
            12: ROVSMS,
        }),
    ),
    graph=graph_011,
)