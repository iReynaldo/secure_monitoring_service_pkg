from pathlib import Path

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import Graph027
from bgp_simulator_pkg import enums

from lib_rovpp import ROVPPV1SimpleAS

from secure_monitoring_service_pkg.tests.system_tests.v4_base_graph_system_tester import V4BaseGraphSystemTester
from secure_monitoring_service_pkg.tests.system_tests.unstable import Unstable
from secure_monitoring_service_pkg.rov_sms import ROVSMS, ROVSMSK1
from secure_monitoring_service_pkg.simulation_framework.scenarios.v4_subprefix_hijack_scenario import V4SubprefixHijack



class BaseHiddenHijackTester(Unstable, V4BaseGraphSystemTester):
    GraphInfoCls = Graph027
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (4, 10, enums.ASNs.VICTIM.value, )


class Test001HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test002HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS


class Test002HiddenHijackROVSMSK1(BaseHiddenHijackTester):
    AdoptASCls = ROVSMSK1
