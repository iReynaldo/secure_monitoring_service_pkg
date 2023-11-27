from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_046
from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.simulation_engine import ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK1

config_133 = EngineTestConfig(
    name="133",
    desc="AutoImmune Attack with V4 Lite k=1",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        AdoptASCls=ROVSMSK1,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            32: ROVSMSK1,
            33: ROVSMSK1,
            77: ROVSimpleAS,
        }),
    ),
    graph=graph_046,
)
