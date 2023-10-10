#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16, 2023

@author: Reynaldo Morillo
"""

from v4_graph_generator import Line, generate_plot, compare_relays_linemap
import data_manager as dm


####################################
# Main
####################################

# Example file name
# V4SubprefixHijackScenario_scenario_none_type_others_policies_real_rov_0_hash_False_probe_twenty_relay_False_attackRelay_1_attacker_2000_trials_full_percentages

#-----------------------------------
# Constants
#-----------------------------------



#-----------------------------------
# Args
#-----------------------------------

scenario = 'V4SubprefixHijackScenario'
scenario_type = 'none'
simulated_policies = 'others' # standard
# rov_setting = 'real'
rov_setting = 'none'
hash_seed = 0
probe = False
# relay
attack_relay = False
num_attackers = 1
num_trials = 8000
adoption_setting = dm.adopting_setting

metric = dm.victim_success
# relays = ['akamai', 'cloudflare', 'verisign', 'incapsula', 'neustar', 'conglomerate']
relays = ['five', 'ten', 'twenty', 'forty']
policy = 'rovppo'
# policy = 'v4'


for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
    
    #-----------------------------------
    # Plot Generation
    #-----------------------------------
    
    # Load paths
    paths = list()
    
    for relay in relays:
        paths.append(
                dm.json_file(scenario, scenario_type, simulated_policies, rov_setting, hash_seed, probe, relay, attack_relay, num_attackers, num_trials)
            )
    
    # Load Results
    subgraph = dm.get_metric_subgraph(metric, adoption_setting)
    results = dm.get_results(paths, subgraph, [dm.policy_name_map[policy]])
    
    
    # Generate Lines
    line_styles_map = dict()
    for i, relay in enumerate(relays):
        line_styles_map[i] = dm.lines_style_mapper(policy, relay)

    lines = []
    for i, result in enumerate(results):
        if result:
            lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
            

    # Set which policy directory the result is saved too
    policy_dir = 'immunity' if policy == 'rovppo' else 'pheme'
    # Set overlay type
    relay_filename = 'cdns' if relays[0] in dm.cdns else 'peers'
        
    # Plot Lines
    generate_plot(lines,
                  ylim=100,
                  outcome_text=dm.metric_outcome[metric],
                  size_inches=(5, 4),
                  linemap=compare_relays_linemap,
                  legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                  fname=f"./immunity_paper_plots/{policy_dir}/subprefix/rov_{rov_setting}/subprefix_{relay_filename}_relay_{dm.metric_filename_prefix[metric]}.pdf")
