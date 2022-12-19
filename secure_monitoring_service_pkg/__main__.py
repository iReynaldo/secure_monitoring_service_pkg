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
    sim_list = list()
    for num_attackers in [2, 3, 5]:
        scenario_list = list()
        for Cls in [ROVSMS, ROVSMSK1, ROVSMSK2, ROVSMSK3, ROVSMSK5, ROVSMSK10]:
            scenario = SubprefixAutoImmuneScenario(AdoptASCls=Cls,
                                                   AnnCls=ROVPPAnn,
                                                   num_attackers=num_attackers)
            scenario_list.append(scenario)
        result_file_name = scenario.name + '_num_attackers_' + str(num_attackers)
        sim = V4Simulation(scenarios=scenario_list,
                           output_path=BASE_PATH / result_file_name,
                           **get_default_kwargs())
        sim_list.append(sim)

    for sim in sim_list:
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
