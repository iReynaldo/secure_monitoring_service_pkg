#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16, 2023

@author: Reynaldo Morillo
"""

from v4_graph_generator import Line, generate_plot, compare_policies_by_attack_relay_linemap, generate_plotly
import data_manager as dm


####################################
# Main
####################################

# Example file name
# V4SubprefixHijackScenario_scenario_none_type_real_rov_0_hash_incapsula_relay_False_attackRelay_5_attacker_500_trials_full_percentages

#-----------------------------------
# Constants
#-----------------------------------



#-----------------------------------
# Args
#-----------------------------------

scenario = 'V4SubprefixHijackScenario'
scenario_type = 'none'
rov_settings = ['none'] # ['none', 'real']
hash_seed = 0
probe = False
tunnel = True
# relay
# attack_relay = False
num_attackers = 1
num_trials = 8000
adoption_setting = dm.adopting_setting

metric = dm.victim_success
relays = ['cloudflare', 'neustar', 'twenty']
policy = 'v4'

for policy in ['v4', 'rovppo']:
    for rov_setting in rov_settings:
        for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
            
            #-----------------------------------
            # Plot Generation
            #-----------------------------------
            
            subgraph = dm.get_metric_subgraph(metric, adoption_setting)
            
            
            # Load paths
            paths = list()
            # Overlay policy path list
            for attack_relay in (False, True):
                for relay in relays:
                    paths.append(
                            dm.json_file(scenario, scenario_type, 'others', rov_setting, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, tunnel=tunnel)
                        )
            
            # Load Results
            results = dm.get_results(paths, subgraph, [dm.policy_name_map[policy]])
            
            # Generate Lines
            line_styles_map = dict()
            i = 0
            for attack_relay in (False, True):
                for relay in relays:
                    line_styles_map[i] = dm.lines_style_mapper(policy, relay, attack_relay)
                    i += 1
            
            lines = []
            for i, result in enumerate(results):
                if result:
                    lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
            
            # Set which policy directory the result is saved too
            policy_dir = 'immunity' if policy == 'rovppo' else 'pheme'
            # Set the mixed adoption setting
            mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
                
            # Plot Lines
            # generate_plotly(lines, metric)
            generate_plot(lines,
                          ylim=100,
                          outcome_text=dm.metric_outcome[metric],
                          linemap=compare_policies_by_attack_relay_linemap,
                          size_inches=(5, 4),
                          legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                          fname=f"./immunity_paper_plots/{policy_dir}/subprefix/{mixed_setting}/subprefix_compare_attack_relay_{dm.metric_filename_prefix[metric]}.pdf")
