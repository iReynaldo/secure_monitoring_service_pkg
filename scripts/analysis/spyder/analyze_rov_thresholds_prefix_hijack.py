#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:04:53 2023

@author: uconn
"""

# %%############################
# Imports
################################


import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio

import data_manager as dm
from v4_graph_generator import rov_color

# %%############################
# Load Data
################################

# Constants
scenario_str = {
    'V4PrefixHijackScenario': 'prefix',
    'V4SubprefixHijackScenario': 'subprefix',
    'RelayPrefixHijack': 'cdn_origin_prefix'
}

# Configure plotting
pio.renderers.default = "browser"

# Parameters
scenario = 'V4PrefixHijackScenario' # 'V4SubprefixHijackScenario'


# Data configuration
# TODO: if needed

# ./jsons/V4PrefixHijackScenario_scenario_none_type_standard_policies_none_rov_0_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_1_attacker_2000_trials_[0.0,0.01]_percentages.csv
rov_data = pd.DataFrame()
for num_attackers in (1, 5):
    rov_data_file_path = f"../../data/graphs/csvs/V4PrefixHijackScenario_scenario_none_type_standard_policies_none_rov_0_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_2000_trials_[0.0,0.01]_percentages.csv"
    rov_raw_data = pd.read_csv(rov_data_file_path, delimiter=",")
    rov_raw_data['num_attackers'] = num_attackers
    rov_data = pd.concat([rov_data, rov_raw_data])

# Load OriginHijack Data
origin_data = pd.DataFrame()
for num_attackers in (1, 5):
    origin_data_file_path = f"../../data/graphs/csvs/V4OriginHijack_scenario_none_type_standard_policies_real_rov_20_conf_True_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_500_trials_full_percentages.csv"
    origin_raw_data = pd.read_csv(origin_data_file_path, delimiter=",")
    origin_raw_data['num_attackers'] = num_attackers
    origin_data = pd.concat([origin_data, origin_raw_data])

# Load Data from CSVs
data = pd.DataFrame()
for num_attackers in (1, 5):
    for thresh in range(0, 110, 10):
        data_file_path = f"../../data/graphs/csvs/{scenario}_scenario_none_type_standard_policies_real_rov_{thresh}_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_2000_trials_[0.0,0.01]_percentages.csv"
        thresh_data = pd.read_csv(data_file_path, delimiter=",")
        thresh_data['thresh'] = thresh
        thresh_data['num_attackers'] = num_attackers
        data = pd.concat([data, thresh_data])


# %%############################
# Preprocessing
################################ 

metric_subgraph_str = {
    dm.attacker_success: 'attacker_success',
    dm.victim_success: 'victim_success',
    dm.disconnections: 'disconnected'    
}


for metric in (dm.attacker_success, dm.victim_success, dm.disconnections):

    # Get the data of interest for plotting
    dataset_agg = (
        data.groupby(
            ["subgraph", "policy", "percentage", "thresh", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_90_per_conf]})
        .reset_index()
    )
    dataset_agg.columns = list(map("".join, dataset_agg.columns.values))
    dataset = dataset_agg.loc[dataset_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    origin_data_agg = (
        origin_data.groupby(
            ["subgraph", "policy", "percentage", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_90_per_conf]})
        .reset_index()
    )
    origin_data_agg.columns = list(map("".join, origin_data_agg.columns.values))
    origin_dataset = origin_data_agg.loc[origin_data_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    rov_data_agg = (
        rov_data.groupby(
            ["subgraph", "policy", "percentage", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_90_per_conf]})
        .reset_index()
    )
    rov_data_agg.columns = list(map("".join, rov_data_agg.columns.values))
    rov_dataset = rov_data_agg.loc[rov_data_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    # %%############################
    # Plotting
    ################################ 
    
    _fig = plt.figure()
    
    # Making an axis instance
    _ax = _fig.add_axes([0, 0, 1, 1])
    
    
    # Make Plot
    colors = {
        1: rov_color,
        5: rov_color
    }
    labels = {
        1: '1 Attacker',
        5: '5 Attackers'
    }
    marker = {
        1: '.',
        5: '*',
    }
    line_style = {
        1:'dotted',
        5: 'solid',
    }
    
    policy = 'rov'
    for num_attackers in (1, 5):
        df = dataset[(dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (dataset.percentage == 0) & (dataset.num_attackers == num_attackers)]
        _ax.errorbar(
            df.thresh,
            df["valuemean"],
            yerr=df["valuecalc_90_per_conf"],
            marker=marker[num_attackers],
            linestyle=line_style[num_attackers],
            color=colors[num_attackers],
            label=labels[num_attackers]
        )
    
    # Add No ROV Curvers
    no_rov_1_attacker = rov_dataset[(rov_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (rov_dataset.percentage == 0) & (rov_dataset.num_attackers == 1)]
    no_rov_5_attacker = rov_dataset[(rov_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (rov_dataset.percentage == 0) & (rov_dataset.num_attackers == 5)]

    _ax.errorbar(
        list(range(0, 110, 10)),
        [ no_rov_1_attacker.iloc[0]['valuemean'] ]*11,
        yerr=[ no_rov_1_attacker.iloc[0]['valuecalc_90_per_conf'] ]*11,
        marker='+',
        linestyle='dotted',
        color="orange",
        label="no ROV, 1 Attacker"
    )
    
    _ax.errorbar(
        list(range(0, 110, 10)),
        [ no_rov_5_attacker.iloc[0]['valuemean'] ]*11,
        yerr=[ no_rov_5_attacker.iloc[0]['valuecalc_90_per_conf'] ]*11,
        marker='x',
        linestyle='solid',
        color="orange",
        label="no ROV, 5 Attackers"
    )
    
    # Add Origin Hijack Curvers
    origin_1_attacker = origin_dataset[(origin_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (origin_dataset.percentage == 0) & (origin_dataset.num_attackers == 1)]
    origin_5_attacker = origin_dataset[(origin_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (origin_dataset.percentage == 0) & (origin_dataset.num_attackers == 5)]

    _ax.errorbar(
        list(range(0, 110, 10)),
        [ origin_1_attacker.iloc[0]['valuemean'] ]*11,
        yerr=[ origin_1_attacker.iloc[0]['valuecalc_90_per_conf'] ]*11,
        marker='s',
        linestyle='dotted',
        color="blue",
        label="1-hop hijack, 1 attacker"
    )
    
    _ax.errorbar(
        list(range(0, 110, 10)),
        [ origin_5_attacker.iloc[0]['valuemean'] ]*11,
        yerr=[ origin_5_attacker.iloc[0]['valuecalc_90_per_conf'] ]*11,
        marker='d',
        linestyle='solid',
        color="blue",
        label="1-hop hijack, 5 attacker"
    )
    
    # if metric == dm.attacker_success:
    #     # Add Line for 
    #     _ax.errorbar(
    #         list(range(0, 110, 10)),
    #         [99.8]*11,
    #         yerr=[0]*11,
    #         marker='^',
    #         linestyle='solid',
    #         color="orange",
    #         label="no ROV, 1 or 5 Attackers"
    #     )
    # else:
    #     _ax.errorbar(
    #         list(range(0, 110, 10)),
    #         [0.1]*11,
    #         yerr=[0]*11,
    #         marker='^',
    #         linestyle='solid',
    #         color="orange",
    #         label="no ROV, 1 or 5 Attackers"
    #     )
    
    # Set Y and X axis Labels
    _ax.set_ylabel(dm.metric_outcome[metric])
    _ax.set_xlabel("Confidence Threshold (%)")
    _ax.legend(loc="best")
    
    # Other plot settings
    _fig.set_dpi(150)
    _fig.set_size_inches(5, 4, forward=True)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().yaxis.grid()
    plt.tight_layout()
    plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
    
    plt.savefig(
        f"./minerva_plots/others/{scenario_str[scenario]}_real_rov_threhsold_{dm.metric_filename_prefix[metric]}.pdf",
        bbox_inches="tight",
    )
