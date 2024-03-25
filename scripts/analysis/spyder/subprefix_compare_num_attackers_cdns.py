#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:36:45 2023

@author: uconn
"""

from v4_graph_generator import Line, generate_plot, generate_plotly, compare_cdns_linemap
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
scenario_type = 'originHijack'  # 'none' # 'originHijack'
rov_settings = ['real', ]
# rov_conf = 90
hash_seed = 0
probe = False
tunnel=True
turnover=True
# relay
attack_relay = True  # TODO: Change this to True
# num_attackers = 1
num_trials = 4000
adoption_setting = dm.non_adopting_setting

metric = dm.victim_success
cdns = ['cloudflare', 'verisign', 'neustar', 'akamai', 'incapsula']
allies = ['five', 'ten', 'twenty']
relays = cdns

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
                paths = list()
                policy_lines = list()
                for relay in relays:
                    for num_attackers in (5, ):
                        paths.append([dm.json_file(scenario, scenario_type, 'v4', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, tunnel=True), ])
                        policy_lines.append( (num_attackers, 'v4', relay) ) 
                        
                # Load Results
                # Policy 1 Resuts
                results = list()
                for path in paths:    
                    results.append(dm.get_results(path, subgraph, [dm.policy_name_map['v4']])[0])
                    
                # Generate Lines
                line_styles_map = dict()
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
                    
                    'Minerva (Sender) Verisign - adopting (1 Attackers)': 'Sender-based CDN (VE), 1 attacker',
                    'Minerva (Sender) Verisign - adopting (5 Attackers)': 'Sender-based CDN (VE), 5 attackers',
                    'Minerva (Sender) Verisign - adopting (10 Attackers)': 'Sender-based CDN (VE), 10 attackers',
                    'Minerva (Sender) Verisign - adopting (20 Attackers)': 'Sender-based CDN (VE), 20 attackers',
                    
                    'Minerva (Sender) Neustar - adopting (1 Attackers)': 'Sender-based CDN (NE), 1 attacker',
                    'Minerva (Sender) Neustar - adopting (5 Attackers)': 'Sender-based CDN (NE), 5 attackers',
                    'Minerva (Sender) Neustar - adopting (10 Attackers)': 'Sender-based CDN (NE), 10 attackers',
                    'Minerva (Sender) Neustar - adopting (20 Attackers)': 'Sender-based CDN (NE), 20 attackers',
                    
                    'Minerva (Sender) Akamai - adopting (1 Attackers)': 'Sender-based CDN (AK), 1 attacker',
                    'Minerva (Sender) Akamai - adopting (5 Attackers)': 'Sender-based CDN (AK), 5 attackers',
                    'Minerva (Sender) Akamai - adopting (10 Attackers)': 'Sender-based CDN (AK), 10 attackers',
                    'Minerva (Sender) Akamai - adopting (20 Attackers)': 'Sender-based CDN (AK), 20 attackers',
                    
                    'Minerva (Sender) Incapsula - adopting (1 Attackers)': 'Sender-based CDN (IN), 1 attacker',
                    'Minerva (Sender) Incapsula - adopting (5 Attackers)': 'Sender-based CDN (IN), 5 attackers',
                    'Minerva (Sender) Incapsula - adopting (10 Attackers)': 'Sender-based CDN (IN), 10 attackers',
                    'Minerva (Sender) Incapsula - adopting (20 Attackers)': 'Sender-based CDN (IN), 20 attackers',
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
                relay_str = 'cdns' if relays == cdns else 'allies'
                scenario_type_str = '' if scenario_type == 'none' else scenario_type
                
                # Plot Lines
                # generate_plotly(lines, metric)
                generate_plot(lines,
                              ylim=100,
                              outcome_text=dm.metric_outcome[metric],
                              size_inches=(5, 4),
                              linemap=compare_cdns_linemap,
                              legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                              # show_legend=(metric ==dm.attacker_success),
                              fname=f"./minerva_plots/others/rov_{rov_conf}/{adoption_setting_str}{scenario_str}_compare_num_attackers_{relay_str}_{scenario_type_str}_{dm.metric_filename_prefix[metric]}.pdf")
                              # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                # generate_plot(lines,
                #               ylim=100,
                #               outcome_text=dm.metric_outcome[metric],
                #               size_inches=(5, 4),
                #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")