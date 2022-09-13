import random
import os
import time

from lib_bgp_simulator import Simulator, BGPAS, MPMethod

from secure_monitoring_service_pkg.simulation_framework.engine_inputs import V4SubprefixHijack
from secure_monitoring_service_pkg.rov_sms import (
    ROVSMSK1,
    ROVSMSK2,
)

from secure_monitoring_service_pkg.simulation_framework.v4_graph import V4Graph


# Set Random Seed to determinitic runs
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)


def main():
    Simulator().run(
        graphs=[
            V4Graph(
                percent_adoptions=[0, 5, 10, 20, 40, 60, 80, 100],
                adopt_as_classes=[ROVSMSK1, ROVSMSK2],
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
        print("Start Time", time.ctime())
        start_time = time.perf_counter()
        main()
    finally:
        end_time = time.perf_counter()
        print("End Time", time.ctime())
        print("Elasped Time: ", end_time - start_time)
