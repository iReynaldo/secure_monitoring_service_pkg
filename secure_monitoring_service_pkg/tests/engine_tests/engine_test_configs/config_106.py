from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_044
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn, ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import V4ScenarioConfig

config_106 = EngineTestConfig(
    name="106",
    desc="Subprefix Hijack with V1 Lite",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        AdoptASCls=ROVPPV1LiteSimpleAS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            1: ROVPPV1LiteSimpleAS,
            8: ROVPPV1LiteSimpleAS,
            7: ROVSimpleAS,
        }),
    ),
    graph=graph_044,
)
