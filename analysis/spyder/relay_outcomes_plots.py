#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:13:27 2023

@author: uconn
"""

from math import sqrt
from statistics import stdev

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

import data_manager as dm
from v4_graph_generator import compare_relays_linemap

###########################
# Constants
###########################

CDNS = ['akamai', 'cloudflare', 'verisign', 'incapsula', 'neustar']
# PEERS = ['five', 'ten', 'twenty']
PEERS = ['five', 'ten']
OUTCOME_MAPS = {
    'attacker_success': 'Attacker Success',
    'successful_connections': 'Successful Connections',
    'disconnections': 'Disconnections'
}

###########################
# Arguments
###########################

relays = PEERS
k_settings = [2, 5, 10]
rov_settings = ['real', 'none']

# TODO: Temp Setting
# k = 2
rov_setting = 'none'

###########################
# Functions
###########################

def get_yerr(list_of_vals):
    """Gets yerr for a single list of values, 90% confidence"""

    if len(list_of_vals) > 1:
        yerr_num = 1.645 * 2 * stdev(list_of_vals)
        yerr_denom = sqrt(len(list_of_vals))
        return yerr_num / yerr_denom
    else:
        return 0


def calculate_outcome(grouped_data, new_col_name, outcome, outcome_column='outcome_before_relay'):
    disconnections_agg_by_trial = grouped_data.aggregate({outcome_column: lambda x: x.eq(outcome).mean()})
    disconnections_agg_by_trial = disconnections_agg_by_trial.reset_index()
    disconnections_agg_by_trial = disconnections_agg_by_trial.rename(columns={outcome_column: new_col_name})

    gb_disconnections_agg_by_trial = disconnections_agg_by_trial.groupby(by=["adoption_setting", "percentage", "relay"])
    disconnections_agg = gb_disconnections_agg_by_trial.aggregate({new_col_name: 'mean'}) * 100
    return disconnections_agg.reset_index()


###########################
# Load Data
###########################
#%%

# Concatenate all the data files
# NOTE: The 'twenty' in peers has some odd rows I couldn't find. So I added dropna to get rid of those odd ones.
relay_df_list = list()
for relay in relays:
    data_file_path = f'../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_{rov_setting}_rov_0_hash_{relay}_relay_False_attackRelay_5_attacker_500_trials_full_percentages_relay_outcomes_metadata.csv'
    relay_df_list.append(pd.read_csv(data_file_path, delimiter='\t'))
data = pd.concat(relay_df_list)
del relay_df_list

# TODO: Temp Setting
# relay_df_list = list()
# for i in range(3):
#     data_file_path = '~/Desktop/graphs/V4SubprefixHijackScenario_scenario_none_type_none_rov_0_hash_neustar_relay_False_attackRelay_5_attacker_2_trials_full_percentages_relay_outcomes_metadata.csv'
#     # data_file_path = '../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_none_rov_0_hash_None_relay_False_attackRelay_5_attacker_500_trials_full_percentages_avoid_list_metadata.csv'
#     relay_df_list.append(pd.read_csv(data_file_path, delimiter='\t'))
# data = pd.concat(relay_df_list)
# del relay_df_list


###########################
# Preprocessing
###########################
#%%

# Convert percentages to whole numbers
data['percentage'] = data['percentage'] * 100

#%%
gb_percentage_and_relay = data.groupby(by=["adoption_setting", "percentage", "relay", "trial"])

# Calculate Attacker Success
attacker_success_agg = calculate_outcome(gb_percentage_and_relay, 'attacker_success', 'Outcomes.ATTACKER_SUCCESS')

# Compute Disconnections
disconnections_agg = calculate_outcome(gb_percentage_and_relay, 'disconnections', 'Outcomes.DISCONNECTED')

# Calculate Successful Connections
successful_connections_agg = calculate_outcome(gb_percentage_and_relay, 'successful_connections', 'Outcomes.VICTIM_SUCCESS')


###########################
# Main
###########################
#%%

for k in k_settings:
    for outcome, agg in [('attacker_success', attacker_success_agg), ('successful_connections', successful_connections_agg), ('disconnections', disconnections_agg)]:
        fig, ax = plt.subplots()
        # Set Plot Style
        plt.tight_layout()
        plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
        plt.legend({'loc':'best', 'prop':{'size': 11}})
        fig.set_size_inches(5, 4, forward=True)
        plt.gca().yaxis.grid()
        fig.set_dpi(150)
        
        # Plot the data
        ax.set_xlabel('Percent adoption')
        ax.set_ylabel(OUTCOME_MAPS[outcome])
        # Add Lines for each version of k
        for relay in relays:
            mask = (agg['adoption_setting'] == f'ROV V4 Lite K{k}') & (agg['relay'] == relay)
            x = agg.loc[mask, 'percentage']
            y = agg.loc[mask, outcome]
            line_label = f'Pheme {relay.capitalize()} - k={k}' if relays == CDNS else f'Pheme Peer {dm.peer_map[relay]} - k={k}'
            ax.errorbar(x, y,  yerr=get_yerr(y),
                        linestyle=compare_relays_linemap[line_label + ' adopting']['linestyle'],
                        color=compare_relays_linemap[line_label + ' adopting']['color'],
                        marker=compare_relays_linemap[line_label + ' adopting']["marker"],
                        label=line_label + ' ASes',
                        path_effects=[path_effects.SimpleLineShadow(offset=(0, -0.5)), path_effects.Normal()])
        
        # Set Y Axis Limits
        bottom, top = plt.ylim()
        if outcome == 'attacker_success':
            plt.ylim(0, 100)
        else:        
            plt.ylim(0, 100)
            
        # Show legend
        ax.legend()
        
        
        # Save the plot
        relay_name = 'cdn' if relays == CDNS else 'peers'
        # plt.show()
        plt.savefig(f'./paper_plots/subprefix/rov_{rov_setting}/subprefix_{relay_name}_relay_k_{k}_outcomes_{outcome}.pdf', bbox_inches='tight')