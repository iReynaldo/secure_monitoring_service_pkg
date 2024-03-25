#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:23:37 2023

@author: uconn
"""

from v4_graph_generator import Line, generate_plot, generate_plotly
import data_manager as dm


paths = ['../../data/graphs/jsons/ArtemisSubprefixHijackScenario_scenario_cdnOnly_type_artemis_policies_real_rov_20_conf_True_turnover_0_hash_False_probe_False_tunnel_verisign_relay_False_attackRelay_5_attacker_500_trials_full_percentages.json',]
metric = dm.victim_success
subgraph = dm.get_metric_subgraph(metric, dm.adopting_setting)

results = dm.get_results(paths, subgraph, [dm.policy_name_map['artemis']])


#%% Plotting
lines = []
for i, result in enumerate(results):
    if result:
        lines.append(Line(dm.lines_style_mapper('artemisCDNOnly', 'neustar'), False, result.adopting[subgraph]))
        
generate_plotly(lines, metric)


