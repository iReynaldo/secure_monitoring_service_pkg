from datetime import datetime
from pathlib import Path
import random
import os
import time
import sys

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS
from secure_monitoring_service_pkg import ROVSMSK1
from secure_monitoring_service_pkg import V4SubprefixHijackScenario


BASE_PATH = Path("~/Desktop/graphs/").expanduser()

# Set Random Seed to make deterministic runs
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)


# Read in arguments
policy_str = sys.argv[1]
perentage = float(sys.argv[2]) / 100.0
num_trials = int(sys.argv[3])

# Interpret the policy_str
if policy_str == "v1":
    policy = ROVPPV1SimpleAS
elif policy_str == "v4":
    policy = ROVSMS
elif policy_str == "v4k1":
    policy = ROVSMSK1
else:
    raise (
        ValueError,
        "Unrecognized policy specified. " "Use following options {v1, v4, v4k1}",
    )


def get_default_kwargs():
    return {
        "percent_adoptions": [perentage],
        "num_trials": num_trials,
        "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
        "parse_cpus": 1,
    }


def main():
    # assert isinstance(input("Turn asserts off for speed?"), str)
    sims = [
        V4Simulation(
            scenarios=[
                V4SubprefixHijackScenario(AdoptASCls=Cls, AnnCls=ROVPPAnn)
                for Cls in [policy]
            ],
            output_path=BASE_PATH / "subprefix",
            **get_default_kwargs(),
        ),
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
