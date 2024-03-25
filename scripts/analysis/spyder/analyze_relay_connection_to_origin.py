#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:23:56 2023

@author: uconn
"""

#%%#############################
# Imports
################################

from collections import Counter
from math import sqrt
from statistics import mean, stdev
from enum import Enum

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

import data_manager as dm

#%%#############################
# Load Data
################################

# Configure plotting
pio.renderers.default = 'browser'

# Parameter
bgp_immunity_policy = 'v4' # 'rovppo'

# Data configuration

# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = '/media/uconn/Seagate Backup Plus Drive/Archives/school_stuff/bgp_immunity/metadata/ArtemisSubprefixHijackScenario_scenario_none_type_artemis_policies_real_rov_20_conf_True_turnover_0_hash_False_probe_True_tunnel_cloudflare_relay_False_attackRelay_5_attacker_500_trials_full_percentages_artemis_metadata.csv'
# data_file_path = f'../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_real_rov_20_conf_True_turnover_0_hash_False_probe_True_tunnel_{relay}_relay_False_attackRelay_5_attacker_{num_trials}_trials_full_percentages_agg_as_metadata.csv'
# data_file_path = f'../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_{tunneled}_tunnel_{relay}_relay_False_attackRelay_1_attacker_{num_trials}_trials_full_percentages_agg_as_metadata.csv'
data = pd.read_csv(data_file_path, delimiter='\t')

# special_data_file_path = '../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_none_rov_0_hash_False_probe_True_tunnel_neustar_relay_False_attackRelay_1_attacker_16000_trials_[0.99]_percentages_agg_as_metadata.csv'
# special_data = pd.read_csv(special_data_file_path, delimiter='\t')

#%% Preview Data Columns
data.columns.to_list()

#%%#############################
# Preprocessing
################################

data['frac_connected_relays'] = data.count_of_cdn_with_successful_path_to_origin / data.num_relays

data_agg = data.groupby(['percentage', 'propagation_round', 'adoption_setting']).agg({'frac_connected_relays': ['mean', dm.calc_90_per_conf]}).reset_index()
data_agg.columns = list(map(''.join, data_agg.columns.values))

#%%#############################
# Plotting
################################


# #%% Matplotlib Line Plot
_fig, _ax = plt.subplots()


# plt.xticks([int(x*100) for x in lines[0]._get_x()])
plt.xticks([0, 20, 40, 60, 80, 100])

# Making an axis instance
_ax = _fig.add_axes([0, 0, 1, 1]) 

feature = 'frac_connected_relays'
_ax.errorbar(data_agg.percentage*100, 
             data_agg[feature+'mean']*100, 
             yerr=data_agg[feature+'calc_90_per_conf']*100)
        
