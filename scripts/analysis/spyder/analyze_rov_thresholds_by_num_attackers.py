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
SUBPREFIX = 'V4SubprefixHijackScenario'
PREFIX = 'V4PrefixHijackScenario'
RELAY_PREFIX = 'RelayPrefixHijack'

scenario_str = {
    PREFIX: 'prefix',
    SUBPREFIX: 'subprefix',
    RELAY_PREFIX: 'cdn_origin_prefix'
}

# Configure plotting
pio.renderers.default = "browser"

# Parameters
num_attackers = 1


# Load No-ROV Data
no_rov_data = pd.DataFrame()
for scenario in ('V4SubprefixHijackScenario', 'V4PrefixHijackScenario'):
    no_rov_data_file_path = f"../../data/graphs/csvs/{scenario}_scenario_none_type_standard_policies_none_rov_0_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_2000_trials_[0.0,0.01]_percentages.csv"
    no_rov_raw_data = pd.read_csv(no_rov_data_file_path, delimiter=",")
    no_rov_raw_data['num_attackers'] = num_attackers
    no_rov_raw_data['scenario'] = scenario
    no_rov_data = pd.concat([no_rov_data, no_rov_raw_data])

# Load OriginHijack Data
origin_data = pd.DataFrame()
origin_data_file_path = f"../../data/graphs/csvs/V4OriginHijack_scenario_none_type_standard_policies_real_rov_20_conf_{num_attackers < 10}_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_500_trials_full_percentages.csv"
origin_raw_data = pd.read_csv(origin_data_file_path, delimiter=",")
origin_raw_data['num_attackers'] = num_attackers
origin_data = pd.concat([origin_data, origin_raw_data])

# Load Data from CSVs
data = pd.DataFrame()
# for scenario in ('V4PrefixHijackScenario', ):
for scenario in ('V4SubprefixHijackScenario', 'V4PrefixHijackScenario'):
    for thresh in range(0, 110, 10):
        data_file_path = f"../../data/graphs/csvs/{scenario}_scenario_none_type_standard_policies_real_rov_{thresh}_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_{num_attackers}_attacker_2000_trials_[0.0,0.01]_percentages.csv"
        thresh_data = pd.read_csv(data_file_path, delimiter=",")
        thresh_data['thresh'] = thresh
        thresh_data['num_attackers'] = num_attackers
        thresh_data['scenario'] = scenario
        data = pd.concat([data, thresh_data])


# %%############################
# Preprocessing
################################ 


metric_subgraph_str = {
    dm.attacker_success: 'attacker_success',
    dm.victim_success: 'victim_success',
    dm.disconnections: 'disconnected'    
}


for metric in (dm.victim_success, ):
# for metric in (dm.attacker_success, dm.victim_success, dm.disconnections):

    # Get the data of interest for plotting
    dataset_agg = (
        data.groupby(
            ["scenario", "subgraph", "policy", "percentage", "thresh", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_per_conf]})
        .reset_index()
    )
    dataset_agg.columns = list(map("".join, dataset_agg.columns.values))
    dataset = dataset_agg.loc[dataset_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    origin_data_agg = (
        origin_data.groupby(
            ["subgraph", "policy", "percentage", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_per_conf]})
        .reset_index()
    )
    origin_data_agg.columns = list(map("".join, origin_data_agg.columns.values))
    origin_dataset = origin_data_agg.loc[origin_data_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    no_rov_data_agg = (
        no_rov_data.groupby(
            ["scenario", "subgraph", "policy", "percentage", "num_attackers"]
        )
        .agg({"value": ["mean", dm.calc_per_conf]})
        .reset_index()
    )
    no_rov_data_agg.columns = list(map("".join, no_rov_data_agg.columns.values))
    no_rov_dataset = no_rov_data_agg.loc[no_rov_data_agg['subgraph'] == f'v4_{metric_subgraph_str[metric]}_all', ] 
    
    # %%############################
    # Plotting
    ################################ 
    
    _fig = plt.figure()
    
    # Making an axis instance
    _ax = _fig.add_axes([0, 0, 1, 1])
    line_width = 3
    
    # Make Plot
    y_axis_label = {
        dm.attacker_success: 'Attacker success (%)', 
        dm.victim_success: 'Successful connection (%)', 
        dm.disconnections: 'Disconnection (%)'
    }
    colors = {
        'rov': rov_color,
        'no_rov': 'C1',
        'origin': 'C0'
    }
    labels = {
        SUBPREFIX: 'sub-prefix hijack, ',
        PREFIX: 'prefix hijack, '
    }
    marker = {
        SUBPREFIX: '.',
        PREFIX: '*',
    }
    line_style = {
        SUBPREFIX:'dotted',
        PREFIX: 'solid',
    }
    
    policy = 'rov'
    for scenario in (PREFIX, SUBPREFIX):
        df = dataset[(dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (dataset.percentage == 0) & (dataset.num_attackers == num_attackers) & (dataset.scenario == scenario)]
        _ax.errorbar(
            df.thresh,
            df["valuemean"],
            yerr=df["valuecalc_per_conf"],
            marker=marker[scenario],
            linestyle=line_style[scenario],
            color=colors['rov'],
            label=labels[scenario] + 'w/ ROV',
            linewidth=line_width
        )
        
        
        if scenario == PREFIX:
            # Add Origin Hijack Curvers
            origin_attacker = origin_dataset[(origin_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (origin_dataset.percentage == 0) & (origin_dataset.num_attackers == num_attackers)]

            _ax.errorbar(
                list(range(0, 110, 10)),
                [ origin_attacker.iloc[0]['valuemean'] ]*11,
                yerr=[ origin_attacker.iloc[0]['valuecalc_per_conf'] ]*11,
                marker='s',
                linestyle='dotted',
                color=colors['origin'],
                label="1-hop attack",
                linewidth=line_width
            )
            
    for scenario in (PREFIX, SUBPREFIX):
        # Add No ROV Curvers
        if scenario == SUBPREFIX:
            if metric == dm.attacker_success:
                # Add Line for 
                _ax.errorbar(
                    list(range(0, 110, 10)),
                    [99.8]*11,
                    yerr=[0]*11,
                    marker='^',
                    linestyle=line_style[scenario],
                    color=colors['no_rov'],
                    label=labels[scenario] + "no ROV",
                    linewidth=line_width
                )
            else:
                _ax.errorbar(
                    list(range(0, 110, 10)),
                    [0.1]*11,
                    yerr=[0]*11,
                    marker='^',
                    linestyle=line_style[scenario],
                    color=colors['no_rov'],
                    label=labels[scenario] + "no ROV",
                    linewidth=line_width
                )
        else:
            no_rov_prefix_attacker = no_rov_dataset[(no_rov_dataset.policy == f"BGP Simple ({dm.policy_name_map[policy]} adopting)") & (no_rov_dataset.percentage == 0) & (no_rov_dataset.num_attackers == num_attackers) & (no_rov_dataset.scenario == scenario)]
            _ax.errorbar(
                list(range(0, 110, 10)),
                [ no_rov_prefix_attacker.iloc[0]['valuemean'] ]*11,
                yerr=[ no_rov_prefix_attacker.iloc[0]['valuecalc_per_conf'] ]*11,
                marker='x',
                linestyle=line_style[scenario],
                color=colors['no_rov'],
                label=labels[scenario] + "no ROV",
                linewidth=line_width
            )
            # _ax.errorbar(
            #     list(range(0, 110, 10)),
            #     [ no_rov_prefix_attacker.iloc[0]['valuemean'] ]*11,
            #     yerr=[ no_rov_prefix_attacker.iloc[0]['valuecalc_per_conf'] ]*11,
            #     marker='x',
            #     linestyle=line_style[scenario],
            #     color=colors['no_rov'],
            #     label=labels[scenario] + "no ROV"
            # )
    
    
    

    
    
    # Set Y and X axis Labels
    _ax.set_ylabel(y_axis_label[metric])
    _ax.set_xlabel("Threshold (%)")
    _ax.legend(loc="best")
    
    # Other plot settings
    _fig.set_dpi(150)
    _fig.set_size_inches(5, 4, forward=True)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().yaxis.grid()
    plt.tight_layout()
    plt.rcParams.update({"font.size": 20, "lines.markersize": 13})
    plt.legend(prop={'size': 15})
    # plt.legend('', frameon=False)  # Remove Legend
    
    plt.savefig(
        f"./minerva_plots/others/compare_hijacks_real_rov_threhsold_{num_attackers}_attackers_{dm.metric_filename_prefix[metric]}.pdf",
        bbox_inches="tight",
    )
