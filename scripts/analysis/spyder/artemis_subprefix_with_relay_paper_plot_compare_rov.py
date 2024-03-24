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

scenario = 'ArtemisSubprefixHijackScenario' # 'V4PrefixHijackScenario'
# scenario_type = 'none'
scenario_type = 'originHijack'  # 'none'  # 'originHijack'
rov_settings = ['real', 'none']
# rov_conf = 20
hash_seed = 0
probe = False
tunnel=True
turnover=True
# relay
attack_relay = True
# num_attackers = 5
num_trials = 500
# adoption_setting = dm.non_adopting_setting

# metric = dm.victim_success
relays = ['cloudflare', ]
# bgp_immunity_policy = 'rovppo'
# policies = ['rov', 'rovppv1lite'].append(bgp_immunity_policy)

for rov_conf in [20, ]:
# for rov_conf in [20, 90, 100]:
    for num_attackers in [5, ]:
    # for num_attackers in [1, 5]:
        for bgp_immunity_policy in ['v4']:
        # for bgp_immunity_policy in ['rovppo', 'v4']:
            # for adoption_setting in [dm.non_adopting_setting, dm.adopting_setting, dm.all_adoption_setting]:
            for adoption_setting in [dm.all_adoption_setting, ]:
                for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
                    
                    #-----------------------------------
                    # Plot Generation
                    #-----------------------------------
                    
                    subgraph = dm.get_metric_subgraph(metric, adoption_setting)
                    
                    
                    # Load paths
                    paths = list()
                    # Standard policies path list
                    # standard_policy_paths = [dm.json_file('V4SubprefixHijackScenario', scenario_type, 'standard', rov_setting, rov_conf, turnover, hash_seed, probe, 'None', False, num_attackers, num_trials)]
                    # Artemis path list
                    artemis_policy_paths = list()
                    for rov_setting in rov_settings:
                        for relay in relays:
                            if relay in dm.cdns:
                                actual_rov_conf = 0 if rov_setting == 'none' else 20
                                artemis_policy_paths.append(
                                        dm.json_file('ArtemisSubprefixHijackScenario', scenario_type, 'artemis', rov_setting, actual_rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                    )
                    artemis_origin_only_policy_paths = list()
                    for rov_setting in rov_settings:
                        for relay in relays:
                            if relay in dm.cdns:
                                if relay == 'cloudflare':
                                    # actual_rov_conf = 0 if rov_setting == 'none' else 20
                                    artemis_origin_only_policy_paths.append(
                                            dm.json_file('ArtemisSubprefixHijackScenario', 'originOnly', 'artemis', rov_setting, rov_conf, turnover, hash_seed, probe, relay, attack_relay, num_attackers, num_trials, False)
                                        )

                    
                    # Load Results
                    # rov_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rov']])
                    # rovpp_results = dm.get_results(standard_policy_paths, subgraph, [dm.policy_name_map['rovppv1lite']])
                    artemis_results = dm.get_results(artemis_policy_paths, subgraph, [dm.policy_name_map['artemis']])
                    artemis_origin_only_results = dm.get_results(artemis_origin_only_policy_paths, subgraph, [dm.policy_name_map['artemis']])

                    # results = rov_results + rovpp_results + artemis_results + artemis_origin_only_results
                    results = artemis_results + artemis_origin_only_results


                    # Generate Lines
                    line_styles_map = dict()                    
                    # Add Artemis
                    index = 0
                    for rov_setting in rov_settings:
                        for relay in relays:
                            if relay in dm.cdns:
                                line_styles_map[index] = dm.lines_style_mapper('artemis', relay, rov_setting=rov_setting)
                                index += 1
                            
                    # artemisOriginOnly
                    for rov_setting in rov_settings:
                        for relay in relays:
                            if relay in dm.cdns:
                                if relay == 'cloudflare':
                                    line_styles_map[index] = dm.lines_style_mapper('artemisOriginOnly', relay, rov_setting=rov_setting)
                                    index += 1
                    
                    lines = []
                    for i, result in enumerate(results):
                        if result:
                            lines.append(Line(line_styles_map[i], False, result.adopting[subgraph]))
                    

                    # Set which policy directory the result is saved too
                    policy_dir = 'immunity' if bgp_immunity_policy == 'rovppo' else 'pheme'
                    # Set the mixed adoption setting
                    mixed_setting = f'rov_{rov_setting}' if rov_setting != 'v4' else 'policy_mixed'
                    adoption_setting_str = {
                        dm.adopting_setting: '',
                        dm.non_adopting_setting: 'non_adopting_',
                        dm.all_adoption_setting: 'all_'
                    }
                    attack_relay_str = 'attack' if attack_relay else 'with'
                    scenario_str = 'prefix' if scenario == 'V4PrefixHijackScenario' else 'subprefix'
                    scenario_type_str = '' if scenario_type == 'none' else f'{scenario_type}_'

                    
                    # Plot Lines
                    generate_plotly(lines, metric)
                    generate_plot(lines,
                                  ylim=100,
                                  outcome_text=dm.metric_outcome[metric],
                                  size_inches=(5, 4),
                                  legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                                  fname=f"./minerva_plots/attackers_{num_attackers}/rov_{rov_conf}/receiver_{adoption_setting_str[adoption_setting]}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{scenario_type_str}{dm.metric_filename_prefix[metric]}.pdf")
                                  # fname=f"./immunity_paper_plots/{policy_dir}/{scenario_str}/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.pdf")
                    # generate_plot(lines,
                    #               ylim=100,
                    #               outcome_text=dm.metric_outcome[metric],
                    #               size_inches=(5, 4),
                    #               legend_kwargs={'loc':'best', 'prop':{'size': 11}},
                    #               fname=f"./immunity_paper_png_plots/{policy_dir}/subprefix/{mixed_setting}/{adoption_setting_str}{scenario_str}_{attack_relay_str}_relay{'_with_probing'if probe else ''}_{dm.metric_filename_prefix[metric]}.png")