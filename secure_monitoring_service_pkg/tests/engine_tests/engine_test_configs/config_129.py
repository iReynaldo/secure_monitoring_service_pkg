from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_045
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn, ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4SubprefixHijackScenario, V4ScenarioConfig

config_129 = EngineTestConfig(
    name="129",
    desc="Subprefix Hijack with V1 Lite",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=V4SubprefixHijackScenario,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        AdoptASCls=ROVPPV1SimpleAS,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            3: ROVPPV1SimpleAS,
            4: ROVPPV1SimpleAS,
            8: ROVPPV1SimpleAS,
            10: ROVPPV1SimpleAS,
            12: ROVPPV1SimpleAS,
            7: ROVSimpleAS,
        }),
    ),
    graph=graph_045,
)
