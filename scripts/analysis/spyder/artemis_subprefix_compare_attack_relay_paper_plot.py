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
rov_settings = ['real', ] # ['none', 'real']
rov_conf = 20
hash_seed = 0
probe = False
tunnel = False
turnover=True
# relay
# attack_relay = False
num_attackers = 5
num_trials = 500
adoption_setting = dm.adopting_setting

metric = dm.victim_success
relays = ['verisign', 'cloudflare', 'twenty']
policy = 'v4'

for rov_conf in (20, ):
    for num_attackers in (5, ):
        for policy in ['v4']:
        # for policy in ['v4', 'rovppo']:
            for rov_setting in rov_settings:
                for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
                    
                    #-----------------------------------
                    # Plot Generation
                    #-----------------------------------
                    
                    subgraph = dm.get_metric_subgraph(metric, adoption_setting)
                    
                    
                    # Load paths
                    
                    # Artemis path list
                    artemis_policy_paths = list()
                    for attack_relay in (False, True):
                        for relay in relays:
                            if relay in dm.cdns:
                                artemis_policy_paths.append(
                                        dm.json_file('ArtemisSubprefixHijackScenario', scenario_type, 'artemis', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                    )
                    
                    # paths = list()
                    # # Overlay policy path list
                    # for attack_relay in (False, True):
                    #     for relay in relays:
                    #         paths.append(
                    #                 dm.json_file(scenario, scenario_type, 'others', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, tunnel=tunnel)
                    #             )
                    
                    # Load 
                    artemis_results = dm.get_results(artemis_policy_paths, subgraph, [dm.policy_name_map['artemis']])
                    # v4_results = dm.get_results(paths, subgraph, [dm.policy_name_map[policy]])
                    
                    # results = v4_results + artemis_results 
                    results = artemis_results 
                    
                    
                    # Generate Lines
                    line_styles_map = dict()
                    i = 0
                    # for attack_relay in (False, True):
                    #     for relay in relays:
                    #         line_styles_map[i] = dm.lines_style_mapper(policy, relay, attack_relay)
                    #         i += 1
                            
                    for attack_relay in (False, True):
                        for relay in relays:
                            if relay in dm.cdns:
                                line_styles_map[i] = dm.lines_style_mapper('artemis', relay, attack_relay)
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
                    generate_plotly(lines, metric)
                    generate_plot(lines,
                                  ylim=100,
                                  outcome_text=dm.metric_outcome[metric],
                                  linemap=compare_policies_by_attack_relay_linemap,
                                  size_inches=(5, 4),
                                  show_legend=True,
                                  legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                                  fname=f"./minerva_plots/attackers_{num_attackers}/rov_{rov_conf}/receiver_subprefix_compare_attack_relay_{dm.metric_filename_prefix[metric]}.pdf")
                                  # fname=f"./immunity_paper_plots/{policy_dir}/subprefix/{mixed_setting}/subprefix_compare_attack_relay_{dm.metric_filename_prefix[metric]}.pdf")
                    # generate_plot(lines,
                    #               ylim=100,
                    #               outcome_text=dm.metric_outcome[metric],
                    #               linemap=compare_policies_by_attack_relay_linemap,
                    #               size_inches=(5, 4),
                    #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                    #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/subprefix_compare_attack_relay_{dm.metric_filename_prefix[metric]}.png")
