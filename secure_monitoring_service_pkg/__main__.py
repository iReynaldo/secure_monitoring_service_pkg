from datetime import datetime
from pathlib import Path
import time
from pathlib import Path
import argparse

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
# Arg Parser
#############################

# def process_args(args):
#     # By default, we're doing the subprefix hijack
#     settings = {"subgraphs": [Cls() for Cls in V4Subgraph.v4_subclasses if Cls.name]}
#     settings["percent_adoptions"] = list(args.percentages)
#     settings["num_trials"] = args.num_trials
#     settings["parse_cpus"] = args.cpus
#
#     # Interpret the policy_str
#     policy = None
#     policy_str = args.policy
#     if policy_str == "v1lite":
#         policy = ROVPPV1LiteSimpleAS
#     elif policy_str == "v4":
#         policy = ROVSMS
#     elif policy_str == "v4k1":
#         policy = ROVSMSK1
#     elif policy_str == "v4k5":
#         policy = ROVSMSK5
#     else:
#         raise (ValueError,
#                "Unrecognized policy specified. "
#                "Use following options {v1, v4, v4k1, v4k5}")
#     return settings, policy, args
#
#
# def parse_args():
#     parser = argparse.ArgumentParser(description='Secure Monitoring Service Simulation')
#     # Simulation Args
#     parser.add_argument('-p', '--percentages',
#                         type=float,
#                         nargs='*',
#                         default=[0.1, 0.2, 0.4, 0.6, 0.8],
#                         help='a list of floats')
#     parser.add_argument('-n', '--num_trials',
#                         type=int,
#                         nargs='?',
#                         default=10,
#                         help='Number of trials to run')
#     parser.add_argument('-c', '--cpus',
#                         type=int,
#                         nargs='?',
#                         default=1,
#                         help='Number of CPUs to use')
#     parser.add_argument('-phs', '--python_hash_seed',
#                         type=int,
#                         nargs='?',
#                         default=0,
#                         help='Deterministic setting seed. '
#                              'Needs to be same as environment '
#                              'variable PYTHONHASHSEED')
#     parser.add_argument('-rov', '--rov_adoption',
#                         type=str,
#                         nargs='?',
#                         default='0',
#                         help='ROV adoption setting. If given, '
#                              'ROV ASes will be added to simulation.',
#                         choices=['real', '5', '10', '15', '20',
#                                  '30', '40', '50', '60', '70', '80', '90'])
#
#     # Scenario Args
#     parser.add_argument('-na', '--num_attackers',
#                         type=int,
#                         nargs='?',
#                         default=1,
#                         help='Number of attackers')
#     parser.add_argument('-asub', '--adoption_subcategory',
#                         type=str,
#                         nargs='*',
#                         default=("stub_or_mh_ases", "etc_ases", "input_clique_ases"),
#                         help='The area in the graph for adoption. '
#                              'Does not restrict additional ROV adoption')
#     parser.add_argument('-relay', '--relay_asns',
#                         type=str,
#                         nargs=2,
#                         default=("stub_or_mh_ases", "etc_ases", "input_clique_ases"),
#                         help='The relays that can be used',
#                         choices=['Caida akamai',
#                                  'Caida cloudflare',
#                                  'Caida verisign',
#                                  'Caida incapsula',
#                                  'Caida neustar',
#                                  'Peer five',
#                                  'Peer ten',
#                                  'Peer twenty',
#                                  'Peer hundred'])
#     parser.add_argument('--assume_relays_are_reachable',
#                         type=bool,
#                         nargs='?',
#                         default=True,
#                         help='This will enable/disable relays from sending '
#                              'out a relay prefix. If set to True, then the '
#                              'relay prefixes are not sent, and relays are'
#                              ' assumed to be reachable to any adopting AS.')
#     parser.add_argument('--tunnel_customer_traffic',
#                         type=bool,
#                         nargs='?',
#                         default=False,
#                         help='Whether or not to allow adopters to tunnel '
#                              'reconnected traffic.')
#     parser.add_argument('-y', '--policy',
#                         type=str,
#                         nargs='?',
#                         default="v4k1",
#                         help='Adoption Policy to use')
#     parser.add_argument('-o', '--output',
#                         type=str,
#                         nargs='?',
#                         default="default",
#                         help='Output filename')
#     parser.add_argument('-s', '--scenario',
#                         type=str,
#                         nargs='?',
#                         default="V4SubprefixHijackScenario",
#                         help='Attack Scenario')
#     return process_args(parser.parse_args())


#############################
# Main Components
#############################


def scenario_kwargs():
    settings = {
        "num_attackers": 5,
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
        "parse_cpus": 2,
        "python_hash_seed": 0,
        "caida_kwargs": {"csv_path": Path("./aux_files/rov_adoption_5.csv")}
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
