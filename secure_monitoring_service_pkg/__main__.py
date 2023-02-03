from datetime import datetime
from pathlib import Path
import time

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1, ROVSMSK2
from secure_monitoring_service_pkg import ROVSMSK3, ROVSMSK5, ROVSMSK6
from secure_monitoring_service_pkg import ROVSMSK10
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg import CDN
from secure_monitoring_service_pkg import Peer


############################
# Constants
############################

BASE_PATH = Path("~/Desktop/graphs/").expanduser()

# Adopting settings
adoption_settings = {
    "adopters_for_1_attackers": [ROVPPV1LiteSimpleAS, ROVSMS, ROVSMSK1, ROVSMSK2],
    "adopters_for_2_attackers": [ROVPPV1LiteSimpleAS, ROVSMSK1, ROVSMSK2, ROVSMSK3],
    "adopters_for_5_attackers": [ROVPPV1LiteSimpleAS, ROVSMSK1, ROVSMSK5, ROVSMSK10]
}


#############################
# Main Components
#############################


def scenario_kwargs():
    settings = {
        "num_attackers": 1,
        "min_rov_confidence": 0,
        "adoption_subcategory_attrs": ("stub_or_mh_ases", "etc_ases", "input_clique_ases"),
        "relay_asns": Peer.twenty,
        "assume_relays_are_reachable": True,
        "tunnel_customer_traffic": False,
    }
    if not (settings["relay_asns"] == Peer.twenty or settings["relay_asns"] == Peer.hundred
    or settings["relay_asns"] == Peer.five or settings["relay_asns"] == Peer.ten):
        assert not settings["assume_relays_are_reachable"], "assume_relays_are_reachable " \
                                                            "should only be set True for " \
                                                            "Peer relay setting"
    return settings


def simulation_kwargs():
    return {
        "percent_adoptions": [0.1, 0.2, 0.4, 0.6, 0.8],
        "num_trials": 1,
        "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
        "parse_cpus": 4,
        "python_hash_seed": 0
    }


def main():
    adoption_classes = adoption_settings[f"adopters_for_{scenario_kwargs()['num_attackers']}_attackers"]
    sims = [
        V4Simulation(scenarios=[SubprefixAutoImmuneScenario(AdoptASCls=Cls,
                                                            AnnCls=ROVPPAnn,
                                                            **scenario_kwargs())
                                for Cls in adoption_classes
                                ],
                     output_path=BASE_PATH / "default",
                     **simulation_kwargs()),
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
