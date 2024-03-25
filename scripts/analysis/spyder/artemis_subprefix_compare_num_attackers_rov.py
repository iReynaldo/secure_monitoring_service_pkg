#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:36:45 2023

@author: uconn
"""

from v4_graph_generator import Line, generate_plot, generate_plotly, receiver_base_compare_rov
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

scenario = 'ArtemisSubprefixHijackScenario' # 'V4PrefixHijackScenario'
scenario_type = 'none' # 'originOnly'
rov_settings = ['real', 'none']
# rov_conf = 90
hash_seed = 0
probe = False
# tunnel=True
turnover=True
# relay
attack_relay = True
# num_attackers = 1
num_trials = 500
# adoption_setting = dm.non_adopting_setting

# metric = dm.victim_success
# relays = ['verisign', 'neustar', 'five', 'twenty']


for rov_conf in [20,]:
    for adoption_setting in [dm.all_adoption_setting]:
        for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
            
            #-----------------------------------
            # Plot Generation
            #-----------------------------------
            
            subgraph = dm.get_metric_subgraph(metric, dm.adopting_setting)
            
            standard_policy_paths = list()
            
            # Load paths                
            paths = list()
            for num_attackers in (1, 20):
                for rov_setting in rov_settings:
                    actual_rov_conf = 0 if rov_setting == 'none' else rov_conf
                    paths.append(
                        dm.json_file(scenario, scenario_type, 'artemis', rov_setting, actual_rov_conf, turnover, hash_seed, probe, 'cloudflare', attack_relay, num_attackers, num_trials, tunnel=False)
                    )

            # Load Results
            # ROVpp Resuts
            results = dm.get_results(paths, subgraph, [dm.policy_name_map['artemis']])
                
            
            # Generate Lines
            line_styles_map = dict()                    
            # Add Artemis
            index = 0
            for num_attackers in (1, 20):
                for rov_setting in rov_settings:
                    line_styles_map[index] = dm.lines_style_mapper('artemis', 'cloudflare', rov_setting=rov_setting, num_attackers=num_attackers)
                    index += 1             
            
            lines = []
            for i, result in enumerate(results):
                if result:
                    lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
            
            # Set which policy directory the result is saved too
            # Set the mixed adoption setting
            mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
            adoption_setting_str = 'non_adopting_' if adoption_setting == dm.non_adopting_setting else '' 
            attack_relay_str = 'attack' if attack_relay else 'with'
            scenario_str = 'prefix' if scenario == 'V4PrefixHijackScenario' else 'subprefix'
            origin_only_str = 'originOnly_' if scenario_type == 'originOnly' else ''
            
            # Plot Lines
            generate_plotly(lines, metric)
            generate_plot(lines,
                          ylim=(0, 100),
                          outcome_text=dm.metric_outcome[metric],
                          size_inches=(5, 4),
                          linemap=receiver_base_compare_rov,
                          legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                          # show_legend=(metric ==dm.attacker_success),
                          fname=f"./minerva_plots/others/rov_{rov_conf}/receiver_{origin_only_str}{adoption_setting_str}{scenario_str}_compare_num_attackers_and_rov_{dm.metric_filename_prefix[metric]}.pdf")
                          # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
            # generate_plot(lines,
            #               ylim=100,
            #               outcome_text=dm.metric_outcome[metric],
            #               size_inches=(5, 4),
            #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
            #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")