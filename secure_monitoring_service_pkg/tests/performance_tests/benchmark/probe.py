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


from rovpp_pkg import ROVPPAnn
from rovpp_pkg import ROVPPV1SimpleAS

from secure_monitoring_service_pkg import V4Subgraph
from secure_monitoring_service_pkg import V4Simulation
from secure_monitoring_service_pkg import ROVSMS, ROVSMSK1
from secure_monitoring_service_pkg import V4SubprefixHijackScenario


BASE_PATH = Path("~/Desktop/graphs/").expanduser()

# Set Random Seed to make deterministic runs
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)


def main(settings, policy):

    # assert isinstance(input("Turn asserts off for speed?"), str)
    sims = V4Simulation(scenarios=[V4SubprefixHijackScenario(AdoptASCls=Cls,
                                                             AnnCls=ROVPPAnn)
                                   for Cls in [policy]
                                   ],
                        output_path=BASE_PATH / "subprefix",
                        **settings),
    for sim in sims:
        sim.run()


def process_args(args):
    # By default we're doing the subprefix hijack
    settings = {"subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name]}
    settings["percent_adoptions"] = list(args.percentages)
    settings["num_trials"] = args.num_trials
    settings["parse_cpus"] = args.cpus

    # Interpret the policy_str
    policy = None
    policy_str = args.policy
    if policy_str == "v1":
        policy = ROVPPV1SimpleAS
    elif policy_str == "v4":
        policy = ROVSMS
    elif policy_str == "v4k1":
        policy = ROVSMSK1
    else:
        raise (ValueError,
               "Unrecognized policy specified. "
               "Use following options {v1, v4, v4k1}")
    return settings, policy, args


def parse_args():
    parser = argparse.ArgumentParser(description='Benchmarking utility')
    parser.add_argument('-p', '--percentages',
                        type=float,
                        nargs='*',
                        default=[0, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1],
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
    # Future feature: specify scenairo
    # parser.add_argument('scenario', '-s', '--scenario',
    #                     type=str,
    #                     nargs=1,
    #                     default="V4SubprefixHijackScenario",
    #                     help='Attack Scenario')
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
    main(settings, policy)
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
        max_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        row = {
            "machine_name": os.uname().nodename,
            "timestamp": timestamp,
            "tag": args.tag,
            "runtime": runtime,
            "max_memory": max_memory,
            "cpus": settings["parse_cpus"],
            "num_trials": settings["num_trials"],
            "hijack_type": "V4SubprefixHijackScenario",
            "policy": args.policy,
            "platform": runtime_platform,
            "platform_version": platform.python_version(),
            "percentages": args.percentages
        }
        writer.writerow(row)
    print("Results written")
