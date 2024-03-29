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
        "rovppo": "BGP Immunity",
        "v4": "Pheme adopting",
        "v4k2": "Pheme k=2 adopting",
        "v4k5": "Pheme k=5 adopting",
        "v4k10": "Pheme k=10 adopting",
    }

#-----------------------------------
# Args
#-----------------------------------

scenario = 'V4SuperprefixPrefixHijack'
scenario_type = 'none'
# rov_setting = 'real'
# rov_setting = 'none'
rov_setting = 'v4'
hash_seed = 0
probe = True
# relay
attack_relay = False
num_attackers = 1
num_trials = 500

metric = dm.victim_success
# k = 5
relays = ['cloudflare', 'verisign', 'five', 'ten', 'twenty']
# policies = ['rov', 'rovppv1lite', f'v4k{k}']
bgp_immunity_policies = ['rovppo']
policies = ['rov', 'rovppv1lite'].extend(bgp_immunity_policies)

for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
    
    #-----------------------------------
    # Plot Generation
    #-----------------------------------
    
    subgraph = dm.metric_subgraph[metric]
    
    
    # Load paths
    paths = list()
    
    for relay in relays:
        paths.append(
                dm.json_file(scenario, scenario_type, rov_setting, hash_seed, probe, relay, attack_relay, num_attackers, num_trials)
            )
    
    # Load Results
    rov_results = dm.get_results([paths[1]], subgraph, [dm.policy_name_map['rov']])
    rovpp_results = dm.get_results([paths[1]], subgraph, [dm.policy_name_map['rovppv1lite']])
    v4_results = dm.get_results(paths, subgraph, [dm.policy_name_map[x] for x in bgp_immunity_policies])
    results = rov_results + rovpp_results + v4_results
    
    # Generate Lines
    lines_map = dict()
    relay_filename = ""
    if bgp_immunity_policies[0] == 'rovppo':
        policy_legend_prefix = 'BGP Immunity'
    else:
        policy_legend_prefix = 'Pheme'
    
    for i, policy in enumerate(['rov', 'rovppv1lite'] + relays):        
        if policy in dm.cdns:
            # lines_map[i] = f"Pheme {policy.capitalize()} - k={k} adopting"
            lines_map[i] = f"{policy_legend_prefix} {policy.capitalize()} - adopting"
            relay_filename = "cdns"
        elif policy in dm.peers:
            # lines_map[i] = f"Pheme Peer {dm.peer_map[policy]} - k={k} adopting"
            lines_map[i] = f"{policy_legend_prefix} Peer {dm.peer_map[policy]} - adopting"
            relay_filename = "peers"
        else:
            lines_map[i] = line_name_map[policy]
    
    lines = []
    for i, result in enumerate(results):
        if result:
            lines.append(Line(lines_map[i], False, result.adopting[subgraph]))
    
    # Set which policy directory the result is saved too
    policy_dir = 'immunity' if bgp_immunity_policies[0] == 'rovppo' else 'pheme'
        
    # Plot Lines
    generate_plot(lines,
                  ylim=100,
                  outcome_text=dm.metric_outcome[metric],
                  size_inches=(5, 4),
                  legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                  fname=f"./immunity_paper_plots/{policy_dir}/superprefix/rov_{rov_setting}/superprefix_with_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
