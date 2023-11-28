from frozendict import frozendict

from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK2

config_140 = EngineTestConfig(
    name="140",
    desc="Subprefix Hijack with V4 Lite k=2",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=3,
        AdoptASCls=ROVSMSK2,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset(graphs.Graph057().attacker_asn_set),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            70: ROVSMSK2,
            71: ROVSMSK2,
            72: ROVSMSK2,
            73: ROVSMSK2,
        }),
    ),
    graph=graphs.graph_057,
)
