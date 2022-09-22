from datetime import datetime
from pathlib import Path

from rovpp_pkg import ROVPPAnn

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
# from secure_monitoring_service_pkg import AttackerSuccessAllSubgraph


BASE_PATH = Path("~/Desktop/graphs/").expanduser()


def get_default_kwargs():
    return {"percent_adoptions": [.5],#[0, .05, .1, .2, .3, .4, .6, .8, 1],
            "num_trials": 1,
            "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
            "parse_cpus": 1}




def main():

    # assert isinstance(input("Turn asserts off for speed?"), str)
    print("Inside Main")
    print(get_default_kwargs()['subgraphs'])
    sims = [
            V4Simulation(scenarios=[V4SubprefixHijackScenario(AdoptASCls=Cls,
                                                              AnnCls=ROVPPAnn)
                                    for Cls in [ROVSMS]
                                    ],
                         output_path=BASE_PATH / "subprefix",
                         **get_default_kwargs()),
           ]

    for sim in sims:
        start = datetime.now()
        sim.run()
        print(f"{sim.output_path} {(datetime.now() - start).total_seconds()}")


if __name__ == "__main__":
    start = datetime.now()
    main()
    print((datetime.now() - start).total_seconds())
