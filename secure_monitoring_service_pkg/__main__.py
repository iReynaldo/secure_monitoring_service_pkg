from datetime import datetime
from pathlib import Path
import random
import os
import time

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1, ROVSMSK2
from secure_monitoring_service_pkg import ROVSMSK3, ROVSMSK5, ROVSMSK10
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario


BASE_PATH = Path("~/Desktop/graphs/").expanduser()

# Set Random Seed to make deterministic runs
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)


def get_default_kwargs():
    return {"percent_adoptions": [0.01, .05, .1, .2, .3, .4, .6, .8, 0.99],
            "num_trials": 5,
            "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
            "parse_cpus": 1}




def main():

    # assert isinstance(input("Turn asserts off for speed?"), str)
    sims = [
        V4Simulation(scenarios=[SubprefixAutoImmuneScenario(AdoptASCls=Cls,
                                                            AnnCls=ROVPPAnn,
                                                            num_attackers=2)
                                for Cls in [ROVSMSK1]
                                ],
                     output_path=BASE_PATH / "autoimmune",
                     **get_default_kwargs()),
    ]

    for sim in sims:
        start = datetime.now()
        sim.run()
        print(f"{sim.output_path} {(datetime.now() - start).total_seconds()}")


if __name__ == "__main__":
    print("Start Time", time.ctime())
    start_time = time.perf_counter()
    try:
        main()
    finally:
        end_time = time.perf_counter()
        print("End Time", time.ctime())
        print("Elasped Time: ", end_time - start_time)
