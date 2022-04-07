from pathlib import Path

import pytest

from lib_bgp_simulator import BaseGraphSystemTester
from lib_bgp_simulator import BGPSimpleAS
from lib_bgp_simulator import ROVSimpleAS
from lib_bgp_simulator import Graph027
from lib_bgp_simulator import enums

from ...unstable import Unstable
from lib_rovpp import ROVPPV1SimpleAS
#from lib_rovpp import ROVPPSubprefixHijack

from .....rov_sms import ROVSMS
from .....engine_inputs import V4SubprefixHijack


class BaseHiddenHijackTester(Unstable, BaseGraphSystemTester):
    GraphInfoCls = Graph027
    BaseASCls = BGPSimpleAS
    EngineInputCls = V4SubprefixHijack
    base_dir = Path(__file__).parent
    adopting_asns = (4, 10, enums.ASNs.VICTIM.value, )


class Test001HiddenHijackROVPPV1(BaseHiddenHijackTester):
    AdoptASCls = ROVPPV1SimpleAS


class Test002HiddenHijackROVSMS(BaseHiddenHijackTester):
    AdoptASCls = ROVSMS

