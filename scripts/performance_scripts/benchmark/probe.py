import time
import csv
import os
import sys
from pathlib import Path
from datetime import datetime
import random
import argparse
import platform
import resource
import subprocess


from rovpp import ROVPPAnn
from rovpp import ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1, ROVSMSK5
from secure_monitoring_service_pkg import V4SubprefixHijackScenario
from secure_monitoring_service_pkg import SubprefixAutoImmuneScenario


BASE_PATH = Path("~/Desktop/graphs/").expanduser()


# Function for this obtained here and updated with more safe function call
# https://stackoverflow.com/a/41210204
def get_git_revision_hash():
  return subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout[:-1]


def get_git_short_revision_hash():
  return subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout[:-1]



def main(settings, policy, scenario):
    scenarios = list()
    if scenario == "V4SubprefixHijackScenario":
        scenarios = v4_subprefix_hijack_scenario(policy)
    elif scenario == "SubprefixAutoImmuneScenario":
        scenarios = subprefix_auto_immune_scenario(policy)
    else:
        raise f"Scenario: '{scenario}' is not recognized"

    sims = V4Simulation(scenarios=scenarios,
                        output_path=BASE_PATH / f"{scenario}_benchmark",
                        **settings),

    for sim in sims:
        sim.run()


def v4_subprefix_hijack_scenario(policy):
    return [
            V4SubprefixHijackScenario(AdoptASCls=Cls,
                                      AnnCls=ROVPPAnn)
            for Cls in [policy]
    ]


def subprefix_auto_immune_scenario(policy):
    return [
        SubprefixAutoImmuneScenario(AdoptASCls=Cls,
                                    AnnCls=ROVPPAnn)
        for Cls in [policy]
    ]


def process_args(args):
    # By default we're doing the subprefix hijack
    settings = {"subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name]}
    settings["percent_adoptions"] = list(args.percentages)
    settings["num_trials"] = args.num_trials
    settings["parse_cpus"] = args.cpus
    # TODO: The following settings are defaults not passed in
    #  These can be added as arguments at a later time.
    settings["caida_kwargs"] = {}  # {"csv_path": Path("./aux_files/rov_adoption_5.csv")}
    settings["python_hash_seed"] = args.seed

    # Interpret the policy_str
    policy = None
    policy_str = args.policy
    if policy_str == "v1":
        policy = ROVPPV1SimpleAS
    elif policy_str == "v4":
        policy = ROVSMS
    elif policy_str == "v4k1":
        policy = ROVSMSK1
    elif policy_str == "v4k5":
        policy = ROVSMSK5
    else:
        raise (ValueError,
               "Unrecognized policy specified. "
               "Use following options {v1, v4, v4k1, v4k5}")
    return settings, policy, args


def parse_args():
    parser = argparse.ArgumentParser(description='Benchmarking utility')
    parser.add_argument('-p', '--percentages',
                        type=float,
                        nargs='*',
                        default=[0.0, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0],
                        help='a list of floats')
    parser.add_argument('-n', '--num_trials',
                        type=int,
                        nargs='?',
                        default=10,
                        help='Number of trials to run')
    parser.add_argument('-c', '--cpus',
                        type=int,
                        nargs='?',
                        default=1,
                        help='Number of CPUs to use')
    parser.add_argument('-y', '--policy',
                        type=str,
                        nargs='?',
                        default="v4k1",
                        help='Adoption Policy to use')
    parser.add_argument('-t', '--tag',
                        type=str,
                        nargs='?',
                        default="standard",
                        help='Tag to put label in benchmark table')
    parser.add_argument('-s', '--scenario',
                        type=str,
                        nargs='?',
                        default="V4SubprefixHijackScenario",
                        help='Attack Scenario')
    parser.add_argument('--seed',
                        type=int,
                        nargs='?',
                        default=0,
                        help='Number of CPUs to use')
    return process_args(parser.parse_args())


if __name__ == "__main__":

    # Parse args and get benchmark settings
    settings, policy, args = parse_args()

    # Track some run time information and print to stdout
    # Track when this was computed
    timestamp = datetime.now().isoformat()
    tsv_start_time = time.perf_counter()
    print("Start Time: ", timestamp)

    # Running Main
    # -----------------------------------------------------------
    main(settings, policy, args.scenario)
    # -----------------------------------------------------------

    # Capture runtime and share with stdout
    runtime = time.perf_counter() - tsv_start_time
    print("End Time: ", datetime.now().isoformat())
    print("Elapsed Time: ", time.perf_counter() - tsv_start_time)
    print("Writing benchmark results to TSV")

    # Save the results of the benchmark to TSV
    with open("results.tsv", "a") as tsvfile:
        fieldnames = [
            "machine_name",
            "os",
            "os_version",
            "git_hash",
            "git_short_hash",
            "timestamp",
            "runtime",
            "max_memory",
            "tag",
            "cpus",
            "num_trials",
            "hijack_type",
            "policy",
            "platform",
            "platform_version",
            "percentages"
        ]
        writer = csv.DictWriter(tsvfile, delimiter="\t", fieldnames=fieldnames)
        # writer.writeheader()  # Comment this out if the file already exists
        # Get the benchmark settings
        runtime_platform = \
            "pypy" if '__pypy__' in sys.builtin_module_names else "python"
        # peak memory usage (kilobytes on Linux, bytes on OS X)
        self_max_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        children_max_memory = \
            resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        total_max_memory = self_max_memory + children_max_memory
        row = {
            "machine_name": os.uname().nodename,
            "os": platform.system(),
            "os_version": platform.release(),
            "git_hash": get_git_revision_hash(),
            "git_short_hash": get_git_short_revision_hash(),
            "timestamp": timestamp,
            "tag": args.tag,
            "runtime": runtime,
            "max_memory": total_max_memory,
            "cpus": settings["parse_cpus"],
            "num_trials": settings["num_trials"],
            "hijack_type": args.scenario,
            "policy": args.policy,
            "platform": runtime_platform,
            "platform_version": platform.python_version(),
            "percentages": args.percentages
        }
        writer.writerow(row)
    print("Results written")
