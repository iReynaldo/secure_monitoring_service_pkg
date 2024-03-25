#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:36:45 2023

@author: uconn
"""

from v4_graph_generator import Line, generate_plot, generate_plotly, num_attackers_linemap
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
scenario_type = 'none'
rov_settings = ['real', ]
# rov_conf = 90
hash_seed = 0
probe = False
tunnel=True
turnover=True
# relay
attack_relay = False
# num_attackers = 1
num_trials = 500
adoption_setting = dm.non_adopting_setting

metric = dm.victim_success
relays = ['verisign', 'neustar', 'five', 'twenty']


for rov_conf in [20,]:
    for adoption_setting in [dm.adopting_setting, dm.all_adoption_setting]:
        for rov_setting in rov_settings:
            for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
                
                #-----------------------------------
                # Plot Generation
                #-----------------------------------
                
                subgraph = dm.get_metric_subgraph(metric, adoption_setting)
                
                standard_policy_paths = list()
                
                # get the ROV and ROV plots  from the function
                # Load paths
                # Standard policies path list
                standard_policy_paths_1 = [dm.json_file(scenario, scenario_type, 'standard', rov_setting, rov_conf, turnover, hash_seed, probe, 'None', False, 1, num_trials)]
                standard_policy_paths_5 = [dm.json_file(scenario, scenario_type, 'standard', rov_setting, rov_conf, turnover, hash_seed, probe, 'None', False, 5, num_trials)]
                # ROVPPO paths
                rovppo_paths_1 =  [dm.json_file(scenario, scenario_type, 'others', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', False, 1, num_trials, tunnel=True)]
                rovppo_paths_5 =  [dm.json_file(scenario, scenario_type, 'others', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', False, 5, num_trials, tunnel=True)]
                # ROVO paths
                rovo_paths_1 =  [dm.json_file(scenario, scenario_type, 'rovo', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', False, 1, num_trials)]
                rovo_paths_5 =  [dm.json_file(scenario, scenario_type, 'rovo', rov_setting, rov_conf, turnover, hash_seed, probe, 'cloudflare', False, 5, num_trials)]
                
                # Load Results
                # ROV Results
                rov_results_1 = dm.get_results(standard_policy_paths_1, subgraph, [dm.policy_name_map['rov']])
                rov_results_5 = dm.get_results(standard_policy_paths_5, subgraph, [dm.policy_name_map['rov']])
                # ROVPPO
                rovppo_results_1 = dm.get_results(rovppo_paths_1, subgraph, [dm.policy_name_map['rovppo']])
                rovppo_results_5 = dm.get_results(rovppo_paths_5, subgraph, [dm.policy_name_map['rovppo']])
                # ROVpp Resuts
                rovpp_results_1 = dm.get_results(standard_policy_paths_1, subgraph, [dm.policy_name_map['rovppv1lite']])
                rovpp_results_5 = dm.get_results(standard_policy_paths_5, subgraph, [dm.policy_name_map['rovppv1lite']])
                # ROVO Results
                rovo_results_1 = dm.get_results(rovo_paths_1, subgraph, [dm.policy_name_map['rovo']])
                rovo_results_5 = dm.get_results(rovo_paths_5, subgraph, [dm.policy_name_map['rovo']])

                # results = rov_results_1 + rov_results_5 + rovpp_results_1 + rovpp_results_5 + rovo_results_1 + rovo_results_5
                # results =  rov_results_5 + rovpp_results_5 + rovo_results_5 + rovppo_results_5
                results =  rov_results_5 + rovpp_results_5 + rovo_results_5 + rovppo_results_5


                
                
                # Generate Lines
                
                line_styles_map = dict()
                # policy_lines = [(1, 'rov'), (5, 'rov'), (1, 'rovppv1lite'), (5, 'rovppv1lite'), (1, 'rovo'), (5, 'rovo')]
                policy_lines = [(5, 'rov'), (5, 'rovppv1lite'), (5, 'rovo'), (5, 'rovppo')]
                index = 0
                for i, policy in enumerate(policy_lines):
                    index = i
                    if policy[1] in dm.standard_policies:
                        line_styles_map[i] = dm.lines_style_mapper(policy[1], policy[1], num_attackers=policy_lines[i][0])
                    else:
                        line_styles_map[i] = dm.lines_style_mapper(policy[1], 'cloudflare', num_attackers=policy_lines[i][0])
                                        
                
                # Adjust Line Labels
                adjust_label_map = {
                    'ROV adopting (1 Attackers)': 'ROV, 1 attacker',
                    'ROV adopting (5 Attackers)': 'ROV, 5 attackers',
                
                    'ROV++ V1 Lite adopting (1 Attackers)': 'ROV++, 1 attacker',
                    'ROV++ V1 Lite adopting (5 Attackers)': 'ROV++, 5 attackers',
                    
                    'ROV Overlayed Cloudflare - adopting (1 Attackers)': 'ROV CDN (CF), 1 attacker',
                    'ROV Overlayed Cloudflare - adopting (5 Attackers)': 'ROV CDN (CF), 5 attackers',
                    
                    'Overlay Cloudflare - adopting (1 Attackers)': 'ROV++ CDN (CF), 1 attacker',
                    'Overlay Cloudflare - adopting (5 Attackers)': 'ROV++ CDN (CF), 5 attackers',
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
                adoption_setting_str = {
                    dm.non_adopting_setting: 'non_adopting_',
                    dm.adopting_setting: '',
                    dm.all_adoption_setting: 'all_'
                }
                attack_relay_str = 'attack' if attack_relay else 'with'
                scenario_str = 'prefix' if scenario == 'V4PrefixHijackScenario' else 'subprefix'
                
                # Plot Lines
                # generate_plotly(lines, metric)
                generate_plot(lines,
                              ylim=100,
                              outcome_text=dm.metric_outcome[metric],
                              size_inches=(5, 4),
                              linemap=num_attackers_linemap,
                              legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                              # show_legend=(metric ==dm.attacker_success),
                              fname=f"./minerva_plots/others/rov_{rov_conf}/{adoption_setting_str[adoption_setting]}{scenario_str}_with_rovo_{dm.metric_filename_prefix[metric]}.pdf")
                              # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                # generate_plot(lines,
                #               ylim=100,
                #               outcome_text=dm.metric_outcome[metric],
                #               size_inches=(5, 4),
                #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")