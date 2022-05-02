from pathlib import Path

import pytest

from lib_bgp_simulator import BaseGraphSystemTester
from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import Graph011

from lib_rovpp import ROVPPV1SimpleAS

from lib_secure_monitoring_service.tests.system_tests.unstable import Unstable
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1
from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack


class BaseHiddenHijackTester(Unstable, BaseGraphSystemTester):
    GraphInfoCls = Graph011
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (5, 6, 1, 11, 12)

class Test007HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test008HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS
