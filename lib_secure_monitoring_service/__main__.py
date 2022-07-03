import random
import os
import time

from lib_bgp_simulator import Simulator, BGPAS, Graph, MPMethod

from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS

from lib_secure_monitoring_service.engine_inputs import V4SubprefixHijack
from lib_secure_monitoring_service.rov_sms import (
    ROVSMS,
    ROVSMSK1,
    ROVSMSK2,
    ROVSMSK3,
    ROVSMSK4,
    ROVSMSK5,
    ROVSMSK6,
    ROVSMSK7,
    ROVSMSK10,
)
from lib_secure_monitoring_service.rov_sms import (
    ROVSMSK20,
    ROVSMSK30,
    ROVSMSK50,
    ROVSMSK70,
    ROVSMSK100,
)
from lib_secure_monitoring_service.rov_sms import (
    ROVSMSK150,
    ROVSMSK200,
    ROVSMSK300,
    ROVSMSK500,
    ROVSMSK1000,
    ROVSMSK2000,
    ROVSMSK5000,
    ROVSMSK20000,
    ROVSMSK30000,
)
from lib_secure_monitoring_service.v4_graph import V4Graph


# Set Random Seed to determinitic runs
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)


def main():
    Simulator().run(
        graphs=[
            V4Graph(
                percent_adoptions=[0, 5, 10, 20, 40, 60, 80, 100],
                adopt_as_classes=[ROVPPV1LiteSimpleAS, ROVSMS],
                EngineInputCls=V4SubprefixHijack,
                num_trials=1000,
                BaseASCls=BGPAS,
                verify_avoid_list=True,
            )
        ],
        mp_method=MPMethod.MP,
    )


if __name__ == "__main__":
    try:
        print("Start Time", time.localtime())
        start_time = time.perf_counter()
        main()
    finally:
        end_time = time.perf_counter()
        print("End Time", time.localtime())
        print("Elasped Time: ", end_time - start_time)
