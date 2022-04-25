from pathlib import Path

import pytest

from lib_bgp_simulator import BaseGraphSystemTester
from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import ROVSimpleAS
from lib_bgp_simulator import Graph040

from ...unstable import Unstable  # NOTE: not sure if this is needed
from lib_rovpp import ROVPPV1SimpleAS

from .....rov_sms import ROVSMS
from .....engine_inputs import V4SubprefixHijack

class BaseHiddenHijackTester(Unstable, BaseGraphSystemTester):
    GraphInfoCls = Graph040
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (32, 33, )
    rov_adopting_asns = (77, )


class Test003HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test004HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS

