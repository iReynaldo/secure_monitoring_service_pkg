from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_043
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn
from secure_monitoring_service_pkg import V4SubprefixHijackScenario, ROVSMSK2
from secure_monitoring_service_pkg import V4ScenarioConfig

config_128 = EngineTestConfig(
    name="128",
    desc="Subprefix Hijack with V4 Lite k=2",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        AdoptASCls=ROVSMSK2,
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
