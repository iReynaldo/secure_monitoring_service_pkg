from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_027
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn
from rovpp import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import V4ScenarioConfig

config_103 = EngineTestConfig(
    name="103",
    desc="Subprefix Hijack with V1 Lite",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        AdoptASCls=ROVPPV1LiteSimpleAS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            4: ROVPPV1LiteSimpleAS,
            10: ROVPPV1LiteSimpleAS,
            ASNs.VICTIM.value: ROVPPV1LiteSimpleAS,
        }),
    ),
    graph=graph_027,
)
