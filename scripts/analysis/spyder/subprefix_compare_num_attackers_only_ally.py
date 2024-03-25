#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:36:45 2023

@author: uconn
"""

from v4_graph_generator import Line, generate_plot, generate_plotly, main_num_attackers_ally_linemap
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

scenario = 'V4SubprefixHijackScenario' # 'V4PrefixHijackScenario'
scenario_type =  'originHijack'  # 'none'
rov_settings = ['real', ]
# rov_conf = 90
hash_seed = 0
probe = False
tunnel=True
turnover=True
# relay
attack_relay = True
# num_attackers = 1
num_trials = 4000
adoption_setting = dm.non_adopting_setting

metric = dm.victim_success
relays = ['verisign', 'neustar', 'five', 'twenty']


for rov_conf in [20,]:
    for adoption_setting in [dm.adopting_setting]:
        for rov_setting in rov_settings:
            for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
                
                #-----------------------------------
                # Plot Generation
                #-----------------------------------
                
                subgraph = dm.get_metric_subgraph(metric, dm.adopting_setting)
                
                standard_policy_paths = list()
                
                # get the ROV and ROV plots  from the function
                # Load paths
                # Policy 1 path list
                # policy_1_1_attacker = [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', attack_relay, 1, num_trials, tunnel=True)]
                # policy_1_5_attacker = [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', attack_relay, 5, num_trials, tunnel=True)]
                # policy_1_10_attacker = [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', attack_relay, 10, num_trials, tunnel=True)]
                # policy_1_20_attacker = [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', attack_relay, 20, num_trials, tunnel=True)]

                # Policy 2 path list
                policy_2_1_attacker =  [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'five', attack_relay, 1, num_trials, tunnel=True)]
                policy_2_5_attacker =  [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'five', attack_relay, 5, num_trials, tunnel=True)]
                policy_2_10_attacker =  [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'five', attack_relay, 10, num_trials, tunnel=True)]
                policy_2_20_attacker =  [dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, 'five', attack_relay, 20, num_trials, tunnel=True)]
                
                # Load Results
                # Policy 1 Resuts
                # policy_1_1_attacker_results = dm.get_results(policy_1_1_attacker, subgraph, [dm.policy_name_map['v4']])
                # policy_1_5_attacker_results = dm.get_results(policy_1_5_attacker, subgraph, [dm.policy_name_map['v4']])
                # policy_1_10_attacker_results = dm.get_results(policy_1_10_attacker, subgraph, [dm.policy_name_map['v4']])
                # policy_1_20_attacker_results = dm.get_results(policy_1_20_attacker, subgraph, [dm.policy_name_map['v4']])
                # Policy 2 Results
                policy_2_1_attacker_results = dm.get_results(policy_2_1_attacker, subgraph, [dm.policy_name_map['v4']])
                policy_2_5_attacker_results = dm.get_results(policy_2_5_attacker, subgraph, [dm.policy_name_map['v4']])
                policy_2_10_attacker_results = dm.get_results(policy_2_10_attacker, subgraph, [dm.policy_name_map['v4']])
                policy_2_20_attacker_results = dm.get_results(policy_2_20_attacker, subgraph, [dm.policy_name_map['v4']])

                # results = rov_results_1 + rov_results_5 + rovpp_results_1 + rovpp_results_5 + rovo_results_1 + rovo_results_5
                # results =  policy_1_1_attacker_results + policy_1_5_attacker_results + policy_1_10_attacker_results + policy_1_20_attacker_results + \
                #     policy_2_1_attacker_results + policy_2_5_attacker_results + policy_2_10_attacker_results + policy_2_20_attacker_results
                results =  policy_2_1_attacker_results + policy_2_5_attacker_results + policy_2_10_attacker_results + policy_2_20_attacker_results
                
                
                # Generate Lines
                
                line_styles_map = dict()
                # policy_lines = [(1, 'rov'), (5, 'rov'), (1, 'rovppv1lite'), (5, 'rovppv1lite'), (1, 'rovo'), (5, 'rovo')]
                policy_lines = [(1, 'v4', 'five'), (5, 'v4', 'five'), (10, 'v4', 'five'), (20, 'v4', 'five'), ]
                index = 0
                for i, policy in enumerate(policy_lines):
                    index = i
                    if policy[1] in dm.standard_policies:
                        line_styles_map[i] = dm.lines_style_mapper(policy[1], policy[1], num_attackers=policy_lines[i][0])
                    else:
                        line_styles_map[i] = dm.lines_style_mapper(policy[1], policy[2], num_attackers=policy_lines[i][0])
                                        
                
                # Adjust Line Labels
                adjust_label_map = {                    
                    'Minerva (Sender) Cloudflare - adopting (1 Attackers)': 'Sender-based CDN (CF), 1 attacker',
                    'Minerva (Sender) Cloudflare - adopting (5 Attackers)': 'Sender-based CDN (CF), 5 attackers',
                    'Minerva (Sender) Cloudflare - adopting (10 Attackers)': 'Sender-based CDN (CF), 10 attackers',
                    'Minerva (Sender) Cloudflare - adopting (20 Attackers)': 'Sender-based CDN (CF), 20 attackers',
                    
                    'Minerva (Sender) Ally 5 - adopting (1 Attackers)': 'Sender-based Ally (k=5), 1 attacker',
                    'Minerva (Sender) Ally 5 - adopting (5 Attackers)': 'Sender-based Ally (k=5), 5 attackers',
                    'Minerva (Sender) Ally 5 - adopting (10 Attackers)': 'Sender-based Ally (k=5), 10 attackers',
                    'Minerva (Sender) Ally 5 - adopting (20 Attackers)': 'Sender-based Ally (k=5), 20 attackers',
                }
                
                lines = []
                for i, result in enumerate(results):
                    if result:
                        new_line = Line(line_styles_map[i], False, result.adopting[subgraph])
                        new_line.label = adjust_label_map[new_line.label]
                        lines.append(new_line)
                        
                
                # Set which policy directory the result is saved too
                # Set the mixed adoption setting
                mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
                adoption_setting_str = 'non_adopting_' if adoption_setting == dm.non_adopting_setting else '' 
                attack_relay_str = 'attack' if attack_relay else 'with'
                scenario_str = 'prefix' if scenario == 'V4PrefixHijackScenario' else 'subprefix'
                scenario_type_str = '' if scenario_type == 'none' else scenario_type
                
                # Plot Lines
                # generate_plotly(lines, metric)
                generate_plot(lines,
                              ylim=(30, 100),
                              outcome_text=dm.metric_outcome[metric],
                              size_inches=(5, 4),
                              linemap=main_num_attackers_ally_linemap,
                              legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                              # show_legend=(metric ==dm.attacker_success),
                              fname=f"./minerva_plots/others/rov_{rov_conf}/{adoption_setting_str}{scenario_str}_compare_num_attackers_ally_{scenario_type_str}_{dm.metric_filename_prefix[metric]}.pdf")
                              # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                # generate_plot(lines,
                #               ylim=100,
                #               outcome_text=dm.metric_outcome[metric],
                #               size_inches=(5, 4),
                #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")