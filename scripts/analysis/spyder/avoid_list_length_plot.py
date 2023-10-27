#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:13:27 2023

@author: uconn
"""

from math import sqrt
from statistics import mean, stdev

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


###########################
# Constants
###########################

# Auxiliary data (i.e. AS degree and rank information)
AUX_DATA_FILE_PATH = './asn_degree_and_rank.csv'


###########################
# Function
###########################

def get_yerr(list_of_vals):
    """Gets yerr for a single list of values, 90% confidence"""

    if len(list_of_vals) > 1:
        yerr_num = 1.645 * 2 * stdev(list_of_vals)
        yerr_denom = sqrt(len(list_of_vals))
        return yerr_num / yerr_denom
    else:
        return 0

###########################
# Load Data
###########################
#%%

data_file_path = '../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_none_rov_0_hash_None_relay_False_attackRelay_5_attacker_500_trials_full_percentages_avoid_list_metadata.csv'
data = pd.read_csv(data_file_path, delimiter='\t')

###########################
# Preprocessing
###########################
#%%

# Convert percentages to whole numbers
data['percentage'] = data['percentage'] * 100

gb_percentage = data.groupby(by=["adoption_setting", "percentage"])
avoid_list_len_agg = gb_percentage.aggregate({"avoid_list_len":"mean"})
avoid_list_len_agg = avoid_list_len_agg.reset_index()

###########################
# Main
###########################
#%%

# Set Plot Style
plt.tight_layout()
plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
plt.legend({'loc':'best', 'prop':{'size': 11}})
fig, ax = plt.subplots()
fig.set_size_inches(5, 4, forward=True)
fig.set_dpi(150)

# Plot the data
ax.set_xlabel('Percent adoption')
ax.set_ylabel('Average Avoid List Size')
# Add Lines for each version of k
for k in [2, 5, 10]:
    mask = avoid_list_len_agg['adoption_setting'] == f'ROV V4 Lite K{k}'
    x = avoid_list_len_agg.loc[mask, 'percentage']
    y = avoid_list_len_agg.loc[mask, 'avoid_list_len']
    ax.errorbar(x, y,  yerr=get_yerr(y),
                marker='.',
                label=f'Pheme k={k}',
                path_effects=[path_effects.SimpleLineShadow(offset=(0, -0.5)), path_effects.Normal()])

# Set Y Axis Limits
bottom, top = plt.ylim()
plt.ylim(0, top)
# Show legend
ax.legend()

# Save the plot
plt.savefig('./paper_plots/subprefix/rov_none/avoid_list_size.pdf', bbox_inches='tight')