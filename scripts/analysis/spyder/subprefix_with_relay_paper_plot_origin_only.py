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
# bgp_immunity_policy = 'rovppo'
# policies = ['rov', 'rovppv1lite'].append(bgp_immunity_policy)

for rov_conf in [20,]:
    for num_attackers in [5,]:
        for bgp_immunity_policy in ['v4']:
        # for bgp_immunity_policy in ['rovppo', 'v4']:
            for adoption_setting in [dm.adopting_setting]:
                for rov_setting in rov_settings:
                    for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
                        
                        #-----------------------------------
                        # Plot Generation
                        #-----------------------------------
                        
                        subgraph = dm.get_metric_subgraph(metric, adoption_setting)
                        
                        
                        # Load paths
                        paths = list()
                        # Standard policies path list
                        standard_policy_paths = [dm.json_file(scenario, scenario_type, 'standard', rov_setting, rov_conf, turnover, hash_seed, probe, 'None', False, num_attackers, num_trials)]
                        # Artemis path list
                        artemis_policy_paths = list()
                        for relay in relays:
                            if relay in dm.cdns:
                                artemis_policy_paths.append(
                                        dm.json_file('ArtemisSubprefixHijackScenario', scenario_type, 'artemis', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                    )
                        # Artemis Origin Only
                        origin_only_paths = list()
                        for relay in relays:
                            origin_only_paths.append(
                                    dm.json_file('ArtemisSubprefixHijackScenario', 'originOnly', 'artemis', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                )
                        # Artemis Origin Only
                        cdn_only_paths = list()
                        for relay in ('verisign', 'neustar', 'cloudflare'):
                            cdn_only_paths.append(
                                    dm.json_file('ArtemisSubprefixHijackScenario', 'cdnOnly', 'artemis', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                )
                        # Overlay policies path list
                        for relay in relays:
                                paths.append(
                                        dm.json_file(scenario, scenario_type, 'others', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, tunnel=tunnel)
                                    )
                        
                        # Load Results
                        rov_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rov']])
                        rovpp_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rovppv1lite']])
                        artemis_results = dm.get_results(artemis_policy_paths, subgraph, [dm.policy_name_map['artemis']])
                        v4_results = dm.get_results(paths, subgraph, [dm.policy_name_map[bgp_immunity_policy]])
                        origin_only_results = dm.get_results(origin_only_paths, subgraph, [dm.policy_name_map['artemis']])
                        cdn_only_results = dm.get_results(cdn_only_paths, subgraph, [dm.policy_name_map['artemis']])
                        results = rov_results + rovpp_results + v4_results + artemis_results + origin_only_results + cdn_only_results
                        
                        # Generate Lines
                        line_styles_map = dict()
                        policy_lines = dm.standard_policies + tuple(relays)
                        index = 0
                        for i, policy in enumerate(policy_lines):
                            index = i
                            if policy in dm.standard_policies:
                                line_styles_map[i] = dm.lines_style_mapper(policy, policy)
                            else:
                                line_styles_map[i] = dm.lines_style_mapper(bgp_immunity_policy, policy)
                        
                        # Add Artemis
                        index += 1
                        for relay in relays:
                            if relay in dm.cdns:
                                line_styles_map[index] = dm.lines_style_mapper('artemis', relay)
                                index += 1
                        
                        # Origin Only
                        for relay in relays:
                            if relay in dm.cdns:
                                line_styles_map[index] = dm.lines_style_mapper('artemisOriginOnly', relay)
                            index += 1
                                
                        # CDN Only
                        for relay in ('verisign', 'neustar', 'cloudflare'):
                            if relay in dm.cdns:
                                line_styles_map[index] = dm.lines_style_mapper('artemisCDNOnly', relay)
                            index += 1
                        
                        lines = []
                        for i, result in enumerate(results):
                            if result:
                                lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
                        
                        # Set which policy directory the result is saved too
                        policy_dir = 'immunity' if bgp_immunity_policy == 'rovppo' else 'pheme'
                        # Set the mixed adoption setting
                        mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
                        adoption_setting_str = 'non_adopting_' if adoption_setting == dm.non_adopting_setting else '' 
                        attack_relay_str = 'attack' if attack_relay else 'with'
                        scenario_str = 'prefix' if scenario == 'V4PrefixHijackScenario' else 'subprefix'
                        
                        # Plot Lines
                        generate_plotly(lines, metric)
                        generate_plot(lines,
                                      ylim=100,
                                      outcome_text=dm.metric_outcome[metric],
                                      size_inches=(5, 4),
                                      legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                                      show_legend=(metric ==dm.attacker_success),
                                      fname=f"./minerva_plots/attackers_{num_attackers}/rov_{rov_conf}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                                      # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                        # generate_plot(lines,
                        #               ylim=100,
                        #               outcome_text=dm.metric_outcome[metric],
                        #               size_inches=(5, 4),
                        #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                        #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")