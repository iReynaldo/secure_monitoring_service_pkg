import random
import os
from lib_bgp_simulator import Simulator, BGPAS, Graph, MPMethod

from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import ROVSMS, ROVSMSK1
from lib_secure_monitoring_service.v4_graph import V4Graph


# Set Random Seed to determinitic runs
os.environ['PYTHONHASHSEED'] = '0'
random.seed(0)


def test_full_scale_verify_avoid_list():
    Simulator().run(graphs=[V4Graph(percent_adoptions=[0,5,10,20,40,60,80,100],
                                    adopt_as_classes=[ROVSMS, ROVSMSK1],
                                    EngineInputCls=V4SubprefixHijack,
                                    num_trials=1,
                                    BaseASCls=BGPAS,
                                    verify_avoid_list=True)],
                    mp_method = MPMethod.SINGLE_PROCESS
                    )
