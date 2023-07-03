#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16, 2023

@author: Reynaldo Morillo
"""

from v4_graph_generator import Line, generate_plot
import data_manager as dm


####################################
# Main
####################################

# Example file name
# V4SubprefixHijackScenario_scenario_none_type_real_rov_0_hash_incapsula_relay_False_attackRelay_5_attacker_500_trials_full_percentages

#-----------------------------------
# Constants
#-----------------------------------

line_name_map = {
        "rov": 'ROV adopting',
        "rovppv1lite": "ROV++ V1 Lite adopting",
        "v4k2": "Pheme k=2 adopting",
        "v4k5": "Pheme k=5 adopting",
        "v4k10": "Pheme k=10 adopting",
    }

#-----------------------------------
# Args
#-----------------------------------

scenario = 'V4SubprefixHijackScenario'
scenario_type = 'none'
# rov_setting = 'real'
rov_setting = 'none'
hash_seed = 0
# relay
attack_relay = False
num_attackers = 5
num_trials = 500

metric = dm.victim_success
# relays = ['cloudflare', 'verisign',]
relay = 'None'
policies = dm.policy_name_map.keys()

for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
    
    #-----------------------------------
    # Plot Generation
    #-----------------------------------
    
    subgraph = dm.metric_subgraph[metric]
    
    
    # Load paths
    paths = list()
    
    paths.append(
            dm.json_file(scenario, scenario_type, rov_setting, hash_seed, relay, attack_relay, num_attackers, num_trials)
        )
    
    # Load Results
    policy_key_values = [dm.policy_name_map[x] for x in policies]
    results = dm.get_results(paths, subgraph, policy_key_values)
    
    
    # Generate Lines
    lines_map = dict()
    relay_filename = ""
    for i, policy in enumerate(policies):
        lines_map[i] = line_name_map[policy]
    # for i, relay in enumerate(relays):
    #     if relay in dm.cdns:
    #         lines_map[i] = f"DAM {relay.capitalize()} - k={k} adopting"
    #         relay_filename = "cdns"
    #     elif relay in dm.peers:
    #         lines_map[i] = f"DAM Peer {dm.peer_map[relay]} - k={k} adopting"
    #         relay_filename = "peers"
    
    lines = []
    for i, result in enumerate(results):
        if result:
            lines.append(Line(lines_map[i], False, result.adopting[subgraph]))
    
        
    # Plot Lines
    generate_plot(lines,
                  ylim=100,
                  outcome_text=dm.metric_outcome[metric],
                  size_inches=(5, 4),
                  legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                  fname=f"./paper_plots/subprefix/rov_{rov_setting}/subprefix_no_relay_{dm.metric_filename_prefix[metric]}.pdf")
