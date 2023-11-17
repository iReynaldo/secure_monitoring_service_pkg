from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_027
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs
from bgpy.simulation_framework import ScenarioConfig

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS

config_104 = EngineTestConfig(
    name="104",
    desc="Subprefix Hijack with V4 Lite.",
    scenario_config=ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AdoptASCls=ROVSMS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            4: ROVSMS,
            10: ROVSMS,
            ASNs.VICTIM.value: ROVSMS,
        }),
    ),
    graph=graph_027,
    propagation_rounds=1,
)