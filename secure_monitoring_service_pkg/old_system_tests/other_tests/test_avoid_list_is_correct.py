import random
import os
from bgp_simulator_pkg import Simulator, BGPAS, MPMethod

from secure_monitoring_service_pkg.simulation_framework.scenarios.v4_subprefix_hijack_scenario import V4SubprefixHijack
from secure_monitoring_service_pkg.rov_sms import ROVSMS, ROVSMSK1
from secure_monitoring_service_pkg.simulation_framework.v4_subgraph import V4Graph


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
