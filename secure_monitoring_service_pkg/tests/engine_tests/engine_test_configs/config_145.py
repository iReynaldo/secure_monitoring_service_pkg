from frozendict import frozendict

from bgpy.tests.engine_tests.utils import EngineTestConfig
from bgpy.simulation_engine import BGPSimpleAS, ROVSimpleAS
from bgpy.enums import ASNs

from rovpp import ROVPPAnn

from .. import graphs
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import V4ScenarioConfig
from secure_monitoring_service_pkg import ROVSMSK3

config_145 = EngineTestConfig(
    name="145",
    desc="AutoImmune Attack with V4 Lite",
    scenario_config=V4ScenarioConfig(
        ScenarioCls=SubprefixAutoImmuneScenario,
        num_attackers=2,
        AdoptASCls=ROVSMSK3,
        BaseASCls=BGPSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset(graphs.Graph059().attacker_asn_set),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            3: ROVSMSK3,
            4: ROVSMSK3,
            8: ROVSMSK3,
            10: ROVSMSK3,
            11: ROVSMSK3,
            7: ROVSimpleAS,
        }),
    ),
    graph=graphs.graph_059,
)
