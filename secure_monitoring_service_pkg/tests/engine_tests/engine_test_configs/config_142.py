from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_043
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMS

config_142 = EngineTestConfig(
    name="142",
    desc="AutoImmune Attack with V4 Lite",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=1,
        AdoptASCls=ROVSMS,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            3: ROVSMS,
            4: ROVSMS,
            8: ROVSMS,
            10: ROVSMS,
            7: ROVSimpleAS,
        }),
    ),
    graph=graph_043,
)
