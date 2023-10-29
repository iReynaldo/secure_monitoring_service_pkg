#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16, 2023

@author: Reynaldo Morillo
"""

from v4_graph_generator import Line, generate_plot, generate_plotly
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
rov_settings = ['none', 'real']
hash_seed = 0
probe = False
# relay
attack_relay = False
num_attackers = 1
num_trials = 8000
adoption_setting = dm.adopting_setting

metric = dm.victim_success
relay = 'None'
bgp_immunity_policy = 'v4'
policies = ['rov', 'rovppv1lite'].append(bgp_immunity_policy)


for rov_setting in rov_settings:
    for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
        
        #-----------------------------------
        # Plot Generation
        #-----------------------------------
        
        subgraph = dm.get_metric_subgraph(metric, adoption_setting)
        
        
        # Load paths
        paths = list()
        # Standard policies path list
        standard_policy_paths = [dm.json_file(scenario, scenario_type, 'standard', rov_setting, hash_seed, probe, 'None', attack_relay, num_attackers, num_trials)]
        # Overlay policies path list
        paths.append(
                dm.json_file(scenario, scenario_type, 'others', rov_setting, hash_seed, probe, relay, attack_relay, num_attackers, num_trials)
            )
        

        # Load Results
        rov_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rov']])
        rovpp_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rovppv1lite']])
        v4_results = dm.get_results(paths, subgraph, [dm.policy_name_map[bgp_immunity_policy]])
        results = rov_results + rovpp_results + v4_results
        
        
        # Generate Lines
        line_styles_map = dict()
        policy_lines = dm.standard_policies + (relay,)
        for i, policy in enumerate(policy_lines):
            if policy in dm.standard_policies:
                line_styles_map[i] = dm.lines_style_mapper(policy, policy)
            else:
                line_styles_map[i] = dm.lines_style_mapper(bgp_immunity_policy, policy)
        
        lines = []
        for i, result in enumerate(results):
            if result:
                lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
        
        # Set which policy directory the result is saved too
        policy_dir = 'immunity' if bgp_immunity_policy == 'rovppo' else 'pheme'
        # Set the mixed adoption setting
        mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
        adoption_setting_str = 'non_adopting_' if adoption_setting == dm.non_adopting_setting else '' 
        
        # Plot Lines
        generate_plotly(lines, metric)
        generate_plot(lines,
                      ylim=100,
                      outcome_text=dm.metric_outcome[metric],
                      size_inches=(5, 4),
                      legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                      fname=f"./immunity_paper_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}subprefix_no_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
