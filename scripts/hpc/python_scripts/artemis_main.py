from datetime import datetime
from pathlib import Path
import time
import sys

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1, ROVSMSK2
from secure_monitoring_service_pkg import ROVSMSK3, ROVSMSK5
from secure_monitoring_service_pkg import ROVSMSK10
from secure_monitoring_service_pkg import Artermis
from secure_monitoring_service_pkg import ArtemisSubprefixHijackScenario
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
    "adopters_for_5_attackers": [ROVPPV1LiteSimpleAS, ROVSMSK1, ROVSMSK5, ROVSMSK10],
}

# Scenario options
AUTOIMMUNE = "SubprefixAutoImmuneScenario"
SUBPREFIX_HIJACK = "V4SubprefixHijackScenario"
ARTEMIS_SUBPREFIX_HIJACK = "ArtemisSubprefixHijackScenario"

############################
# Args
############################

cdn_arg = sys.argv[1]
num_attackers = int(sys.argv[2])

#############################
# Functions
#############################


def process_experiment_settings(simulation_kwargs, scenario_kwargs, other_settings):
    settings = dict()
    settings.update(other_settings)
    del simulation_kwargs["subgraphs"]  # We don't need to output this
    simulation_kwargs["caida_kwargs"] = str(simulation_kwargs["caida_kwargs"])
    settings.update(simulation_kwargs)
    scenario_kwargs["relay_asns"] = (
        list(scenario_kwargs["relay_asns"])
        if len(scenario_kwargs["relay_asns"]) <= 5
        else [
            len(scenario_kwargs["relay_asns"]),
        ]
    )
    settings.update(scenario_kwargs)
    return settings


#############################
# Simulation Arguments
#############################


def other_settings():
    settings = {
        "scenario": ARTEMIS_SUBPREFIX_HIJACK,
        "output_filename": f"artemis_{cdn_arg}_cdn",
    }
    return settings


def scenario_kwargs():
    settings = {
        "num_attackers": num_attackers,
        "min_rov_confidence": 1000,
        "adoption_subcategory_attrs": (
            "stub_or_mh_ases",
            "etc_ases",
            "input_clique_ases",
        ),
        "relay_asns": getattr(CDN, cdn_arg),
        "assume_relays_are_reachable": False,
        "tunnel_customer_traffic": False,
    }
    # Set for AutoImmune attack indirect/direct
    if other_settings()["scenario"] == AUTOIMMUNE:
        settings["indirect"] = False

    # Validate Settings
    if not (
        settings["relay_asns"] == Peer.twenty
        or settings["relay_asns"] == Peer.hundred
        or settings["relay_asns"] == Peer.five
        or settings["relay_asns"] == Peer.ten
    ):
        assert not settings["assume_relays_are_reachable"], (
            "assume_relays_are_reachable "
            "should only be set True for "
            "Peer relay setting"
        )
    return settings


def simulation_kwargs():
    return {
        "percent_adoptions": [0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.99],
        "num_trials": 500,
        "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
        "parse_cpus": 160,
        "python_hash_seed": 0,
        "caida_kwargs": {},  # {"csv_path": Path("./aux_files/rov_adoption_5.csv")}
    }


#############################
# Main
#############################


def main():
    # Load Simulation settings
    settings = other_settings()
    settings["output_filename"] = (
        settings["output_filename"]
        + f"_{scenario_kwargs()['num_attackers']}_attacker"
        + f"_{simulation_kwargs()['num_trials']}_trials"
    )

    # Create Sim
    sims = [
        V4Simulation(
            scenarios=[
                ArtemisSubprefixHijackScenario(
                    AdoptASCls=Cls, AnnCls=ROVPPAnn, **scenario_kwargs()
                )
                for Cls in [
                    Artermis,
                ]
            ],
            output_path=BASE_PATH / settings["output_filename"],
            **simulation_kwargs(),
        ),
    ]

    # collect experiment settings
    experiment_settings_to_save = process_experiment_settings(
        simulation_kwargs(), scenario_kwargs(), settings
    )

    # Run Simulations
    for sim in sims:
        start = datetime.now()
        sim.run(experiment_settings_to_save)
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
