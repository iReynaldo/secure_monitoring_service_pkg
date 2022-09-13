from pathlib import Path

from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import Graph041

from lib_rovpp import ROVPPV1SimpleAS

from secure_monitoring_service_pkg.tests.system_tests.v4_base_graph_system_tester import V4BaseGraphSystemTester
from secure_monitoring_service_pkg.tests.system_tests.unstable import Unstable
from secure_monitoring_service_pkg.rov_sms import ROVSMS
from secure_monitoring_service_pkg.simulation_framework.engine_inputs import V4SubprefixHijack


class BaseHiddenHijackTester(Unstable, V4BaseGraphSystemTester):
    GraphInfoCls = Graph041
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (32, 33, 55, )
    rov_adopting_asns = (77, )


class Test003HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test004HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS

