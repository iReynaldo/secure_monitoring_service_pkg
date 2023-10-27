#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:12:16 2023

@author: Reynaldo Morillo

This module helps access the data for plotting
"""

import json
from math import sqrt

import numpy as np

from v4_graph_generator import PolicyResult


############################
# Constants
############################

BASE_FILE_PATH = "../../data/graphs/jsons"
BASE_METADATA_FILE_PATH = "../../data/graphs/metadata"

cdns = ("akamai", "cloudflare", "verisign", "incapsula", "neustar", "conglomerate")
peers = ("five", "ten", "twenty", "forty", "fifty", "hundred")

standard_policies = ("rov", "rovppv1lite")

adopting_setting = "adopting"
non_adopting_setting = "non_adopting"

# Topology Stats
# Number of ASes in topology section
num_stubs_of_multihomed_ases = 63687
num_etc_ases = 11668
num_input_clique_ases = 19
num_all_ases = 75374

# Policy Settings
# 'standard': includes results for only ROV and ROV++ v1 Lite
# 'others': Any other policies run, which in this case is just BGP Immunity Overlayed and BGP Immunity w/ Monitoring Systemz
policy_settings = ("standard", "others")

attacker_success = "attacker_success"
victim_success = "victim_success"
disconnections = "disconnections"

metric_outcome = {
    attacker_success: "Attacker Success",
    victim_success: "Successful Connections",
    disconnections: "Disconnections",
}

metric_filename_prefix = {
    attacker_success: "attacker_success",
    victim_success: "successful_connections",
    disconnections: "disconnections",
}

# For indexing in JSON file
policy_name_map = {
    "rov": "ROVSimple",
    "rovppv1lite": "ROV++V1 Lite Simple",
    "rovppo": "ROV++ V1 Lite Simple Overlayed",
    "v4": "ROV V4 Lite",
    "v4k2": "ROV V4 Lite K2",
    "v4k5": "ROV V4 Lite K5",
    "v4k10": "ROV V4 Lite K10",
}

peer_map = {
    "five": 5,
    "ten": 10,
    "twenty": 20,
    "forty": 40,
    "fifty": 50,
    "hundred": 100,
}


############################
# Functions
############################


def calc_90_per_conf(list_of_vals):
    if len(list_of_vals) > 1:
        yerr_num = 1.645 * 2 * np.std(list_of_vals)
        yerr_denom = sqrt(len(list_of_vals))
        return yerr_num / yerr_denom
    else:
        return 0


# TODO: Not done implementing
def get_metadata(
    scenario,
    scenario_type,
    policies,
    rov_setting,
    hash_seed,
    probe,
    relay,
    attack_relay,
    num_attackers,
    num_trials,
    tunnel=False,
    percentages="full",
):
    return (
        f"{BASE_METADATA_FILE_PATH}/"
        f"{scenario}_scenario"
        f"_{scenario_type}_type"
        f"_{policies}_policies"
        f"_{rov_setting}_rov"
        f"_{hash_seed}_hash"
        f"_{probe}_probe{'_True_tunnel' if tunnel else ''}"
        f"_{relay}_relay"
        f"_{attack_relay}_attackRelay"
        f"_{num_attackers}_attacker"
        f"_{num_trials}_trials"
        f"_{percentages}_percentages.json"
    )


def get_metric_subgraph(metric, adoption_setting):
    metric_subgraph = {
        attacker_success: f"v4_attacker_success_{adoption_setting}_stubs_and_multihomed",
        victim_success: f"v4_victim_success_{adoption_setting}_stubs_and_multihomed",
        disconnections: f"v4_disconnected_{adoption_setting}_stubs_and_multihomed",
    }
    return metric_subgraph[metric]


# For mapping the styles to the lines
def lines_style_mapper(policy, relay, attack_relay=False):
    if relay in cdns:
        relay_setting = f" {relay.capitalize()} -"
    elif relay in peers:
        relay_setting = f" Ally {peer_map[relay]} -"
    else:
        relay_setting = ""
    mapping = {
        "rov": "ROV",
        "rovppv1lite": "ROV++ V1 Lite",
        "rovppo": "BGPIm",
        "v4": "BGPImMS",
        "v4k2": "BGPImMS k=2",
        "v4k5": "BGPImMS k=5",
        "v4k10": "BGPImMS k=10",
    }
    attack_relay_str = " Attacked" if attack_relay else ""
    return mapping[policy] + attack_relay_str + relay_setting + " adopting"


############################
# Functions
############################


def json_file(
    scenario,
    scenario_type,
    policies,
    rov_setting,
    hash_seed,
    probe,
    relay,
    attack_relay,
    num_attackers,
    num_trials,
    tunnel=False,
    percentages="full",
):
    # V4SubprefixHijackScenario_scenario_none_type_others_policies_real_rov_0_hash_False_probe_twenty_relay_False_attackRelay_1_attacker_2000_trials_full_percentages
    # if relay == 'twenty':
    #     hash_seed = 10
    return (
        f"{BASE_FILE_PATH}/"
        f"{scenario}_scenario"
        f"_{scenario_type}_type"
        f"_{policies}_policies"
        f"_{rov_setting}_rov"
        f"_{hash_seed}_hash"
        f"_{probe}_probe"
        f"_{tunnel}_tunnel"
        f"_{relay}_relay"
        f"_{attack_relay}_attackRelay"
        f"_{num_attackers}_attacker"
        f"_{num_trials}_trials"
        f"_{percentages}_percentages.json"
    )


def get_results(paths, subgraph, policies):
    results = []
    for path in paths:
        json_data = []
        try:
            with open(path, "r") as json_file:
                json_data.append(json.load(json_file))
                for policy in policies:
                    result = PolicyResult(
                        subgraph, "0", "BGP Simple", policy, json_data
                    )
                    results.append(result)
        except (FileNotFoundError, KeyError):
            results.append(None)
    return results
