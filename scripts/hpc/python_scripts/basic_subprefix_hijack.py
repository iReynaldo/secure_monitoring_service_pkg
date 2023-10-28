from datetime import datetime
from pathlib import Path
import time
import sys

from bgpy import ROVSimpleAS

from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1, ROVSMSK2
from secure_monitoring_service_pkg import ROVSMSK3, ROVSMSK5
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
    "adopters_for_1_attackers": [ROVSimpleAS, ROVPPV1LiteSimpleAS, ROVSMS],
    "adopters_for_2_attackers": [
        ROVSimpleAS,
        ROVPPV1LiteSimpleAS,
        ROVSMSK1,
        ROVSMSK2,
        ROVSMSK3,
    ],
    "adopters_for_5_attackers": [
        ROVSimpleAS,
        ROVPPV1LiteSimpleAS,
        ROVSMSK2,
        ROVSMSK5,
        ROVSMSK10,
    ],
}

# Scenario options
AUTOIMMUNE = "SubprefixAutoImmuneScenario"
SUBPREFIX_HIJACK = "V4SubprefixHijackScenario"


############################
# Arguments
############################

if len(sys.argv) != 5:
    raise "This script needs 3 arguments " "[rov setting, overlay setting, attack/no-attacker relay]"

python_hash_seed = int(sys.argv[1])

rov_setting_raw = sys.argv[2].lower()  # none / real
if rov_setting_raw == "none":
    rov_setting = False
elif rov_setting_raw == "real":
    rov_setting = True
else:
    raise "Unknown ROV setting given"

overlay_setting_raw = sys.argv[
    3
].lower()  # None, akamai, cloudflare ..., five, ten, twenty, ...
if overlay_setting_raw == "none":
    overlay_setting = None
elif overlay_setting_raw in [
    "akamai",
    "cloudflare",
    "verisign",
    "incapsula",
    "neustar",
]:
    overlay_setting = CDN().__getattribute__(overlay_setting_raw)
elif overlay_setting_raw in ["five", "ten", "twenty", "hundred"]:
    overlay_setting = Peer().__getattribute__(overlay_setting_raw)
else:
    raise "Unknown Overlay setting given"

attack_relay_raw = sys.argv[4].lower()  # True / False
if attack_relay_raw == "true":
    attack_relay = True
elif attack_relay_raw == "false":
    attack_relay = False
else:
    raise "Unknown attack_relay setting given"


#############################
# Functions
#############################


def process_experiment_settings(simulation_kwargs, scenario_kwargs, other_settings):
    settings = dict()
    settings.update(other_settings)
    del simulation_kwargs["subgraphs"]  # We don't need to output this
    simulation_kwargs["caida_kwargs"] = str(simulation_kwargs["caida_kwargs"])
    settings.update(simulation_kwargs)
    if scenario_kwargs["relay_asns"]:
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
        "scenario": SUBPREFIX_HIJACK,
        "output_filename": "basic_subprefix_hijack_with_rov_v1lite_k2-5-10",
    }
    return settings


def scenario_kwargs():
    settings = {
        "num_attackers": 5,
        "min_rov_confidence": 0 if rov_setting else 1000,
        "adoption_subcategory_attrs": (
            "stub_or_mh_ases",
            "etc_ases",
            "input_clique_ases",
        ),
        "relay_asns": overlay_setting,
        "assume_relays_are_reachable": False,
        "tunnel_customer_traffic": False,
    }
    # Set for AutoImmune attack indirect/direct
    if other_settings()["scenario"] == AUTOIMMUNE:
        settings["indirect"] = False

    return settings


def simulation_kwargs():
    return {
        "percent_adoptions": [0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.99],
        "num_trials": 50,
        "subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name],
        "parse_cpus": 250,
        "python_hash_seed": python_hash_seed,
        "caida_kwargs": {"csv_path": Path("../../../aux_files/rov_adoption_real.csv")}
        if rov_setting
        else {},
    }


#############################
# Main
#############################


def main():
    # Get adoption classes
    adoption_classes = adoption_settings[
        f"adopters_for_{scenario_kwargs()['num_attackers']}_attackers"
    ]

    # Load Simulation settings
    settings = other_settings()
    settings["output_filename"] = (
        settings["output_filename"]
        + f"_{python_hash_seed}_hash"
        + f"_{overlay_setting_raw}_relay"
        + f"_{scenario_kwargs()['num_attackers']}_attacker"
        + f"_{simulation_kwargs()['num_trials']}_trials"
    )

    sims = None
    if settings["scenario"] == SUBPREFIX_HIJACK:
        sims = [
            V4Simulation(
                scenarios=[
                    V4SubprefixHijackScenario(
                        AdoptASCls=Cls, AnnCls=ROVPPAnn, **scenario_kwargs()
                    )
                    for Cls in adoption_classes
                ],
                output_path=BASE_PATH / settings["output_filename"],
                **simulation_kwargs(),
            ),
        ]
    elif settings["scenario"] == AUTOIMMUNE:
        sims = [
            V4Simulation(
                scenarios=[
                    SubprefixAutoImmuneScenario(
                        AdoptASCls=Cls, AnnCls=ROVPPAnn, **scenario_kwargs()
                    )
                    for Cls in adoption_classes
                ],
                output_path=BASE_PATH / settings["output_filename"],
                **simulation_kwargs(),
            ),
        ]
    else:
        raise f"Unknown scenario specified: {settings['scenario']}"

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
