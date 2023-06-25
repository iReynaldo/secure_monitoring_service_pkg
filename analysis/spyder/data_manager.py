#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:12:16 2023

@author: Reynaldo Morillo

This module helps access the data for plotting
"""

import json
from v4_graph_generator import PolicyResult


############################
# Constants
############################

BASE_FILE_PATH = "../../data/graphs/jsons"


attacker_success = "attacker_success"
victim_success = "victim_success"
disconnections = "disconnections"

metric_outcome = {
        attacker_success: "Attacker Success",
        victim_success: "Successful Connections",
        disconnections: "Disconnections"
    }

metric_filename_prefix = {
        attacker_success: "attacker_success",
        victim_success: "successful_connections",
        disconnections: "disconnections"
    }

metric_subgraph = {
        attacker_success: "v4_attacker_success_adopting_stubs_and_multihomed",
        victim_success: "v4_victim_success_adopting_stubs_and_multihomed",
        disconnections: "v4_disconnected_adopting_stubs_and_multihomed"
    }


policy_name_map = {
        "rov": "ROVSimple",
        "rovppv1lite": "ROV++V1 Lite Simple",
        "v4k2": "ROV V4 Lite K2",
        "v4k5": "ROV V4 Lite K5",
        "v4k10": "ROV V4 Lite K10",
    }

peer_map = {
        "five": 5,
        "ten": 10,
        "twenty": 20
    }

cdns = ('akamai', 'cloudflare', 'verisign', 'incapsula', 'neustar')
peers = ('five', 'ten', 'twenty')


############################
# Functions
############################

def json_file(scenario, scenario_type, rov_setting, hash_seed, 
              relay, attack_relay, num_attackers, num_trials, percentages="full"):
    # if relay == 'twenty':
    #     hash_seed = 10
    return f"{BASE_FILE_PATH}/" \
           f"{scenario}_scenario" \
           f"_{scenario_type}_type" \
           f"_{rov_setting}_rov" \
           f"_{hash_seed}_hash" \
           f"_{relay}_relay" \
           f"_{attack_relay}_attackRelay" \
           f"_{num_attackers}_attacker" \
           f"_{num_trials}_trials" \
           f"_{percentages}_percentages.json"


def get_results(paths, subgraph, policies):
    results = []
    for path in paths:
        json_data = []
        try:
            with open(path, "r") as json_file:
                json_data.append(json.load(json_file))
                for policy in policies:
                    result = PolicyResult(subgraph, "0", "BGP Simple", policy, json_data)
                    results.append(result)
        except (FileNotFoundError, KeyError):
            results.append(None)
    return results
