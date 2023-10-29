#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:34:27 2023

@author: uconn
"""

#%%#############################
# Imports
################################

from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

#%%#############################
# Load Data and configuration
################################

# Configure plotting
pio.renderers.default = 'browser'

# Data configuration
rov_setting = 'none'

# Load data
data_file_path = f'../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_1_attacker_8000_trials_full_percentages_avoid_list_metadata.csv'
data = pd.read_csv(data_file_path, delimiter='\t')

#%% Preview Data Columns
data.columns.to_list()

#%%#############################
# Preprocessing
################################

# #%% Calculate Basic Stats on Avoid List Length
# len_group = data.groupby(['percentage', 'propagation_round', 'adoption_setting']).agg({'avoid_list_len': ['min', 'median', 'mean', 'max', 'std']})


# # Produce the data structure to make a histogram from avoid list data
# #%% Convert avoid list to sets
# data['avoid_list'] = data['avoid_list'].apply(eval)

# #%% Count
# counts = Counter()
# data['avoid_list'].agg(counts.update)

# #%%
# # counts.most_common(25)
# counts_df = pd.DataFrame.from_dict(counts, orient='index').reset_index()
# counts_df = counts_df.rename(columns={'index':'as', 0:'count'})

# #%%
# counts_df = counts_df.sort_values(by=['count'], ascending=False)

# #%%
# top_25_df = counts_df.head(25)
# top_25_df['as'] = top_25_df['as'].astype(str)

# #%%
# counts_df_copy = counts_df
# counts_df_copy['as'] = counts_df_copy['as'].astype(str)

#%%#############################
# Plotting
################################

#%% Box Plot
# fig = px.box(data, x='percentage', y='avoid_list_len')
# fig.show()

#%% Box Plot with matplotlib

# Help from the following guide
# https://www.scaler.com/topics/matplotlib/boxplot-matplotlib/

# Re-organize data into array
box_plot_data = [data.loc[data['percentage'] == 0.01 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.05 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.1 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.2 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.4 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.6 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.8 ,'avoid_list_len'],
                 data.loc[data['percentage'] == 0.99 ,'avoid_list_len']]
_fig = plt.figure() 
 
# Making an axis instance
_ax = _fig.add_axes([0, 0, 1, 1]) 

# Make Plot
_bp = _ax.boxplot(box_plot_data, patch_artist = True, labels=data['percentage'].unique()*100)

# Change the Width of the median line
for median in _bp['medians']:
    median.set(linewidth=2)
    
# Change Flier properties
for flier in _bp['fliers']: flier.set(color ='#e7298a', alpha = 0.01) 

# Set Y and X axis Labels
_ax.set_ylabel(f"Number of ASes on Avoid List")
_ax.set_xlabel("Percent adoption")


_fig.set_dpi(150)
_fig.set_size_inches(5, 4, forward=True)
plt.gca().yaxis.grid()
plt.tight_layout()
plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
plt.savefig(f"./immunity_paper_plots/pheme/subprefix/rov_{rov_setting}/avoid_list_boxplot.pdf", bbox_inches='tight')

#%% Histogram
# fig = px.bar(counts_df_copy, x='as', y='count')
# fig.update_traces(marker_color='rgb(255,0,0)', opacity=0.8)
# fig.show()


