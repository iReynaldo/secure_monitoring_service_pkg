from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_027
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import ROVSMS
from secure_monitoring_service_pkg import V4ScenarioConfig

config_104 = EngineTestConfig(
    name="config_104",
    desc="Subprefix Hijack with V4 Lite.",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AdoptASCls=ROVSMS,
        AnnCls=ROVPPAnn,
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