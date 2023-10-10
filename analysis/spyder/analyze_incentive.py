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

# Data configuration
relay = 'neustar'
rov_setting = 'none'
num_trials = 250
tunneled = True

# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = f'../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_{tunneled}_tunnel_{relay}_relay_False_attackRelay_1_attacker_{num_trials}_trials_full_percentages_agg_as_metadata.csv'
data = pd.read_csv(data_file_path, delimiter='\t')

#%% Preview Data Columns
data.columns.to_list()

#%%#############################
# Preprocessing
################################

#%%-----------------------------
# Classes, Enums, and  Funcs
#-------------------------------

class ProviderSetting(Enum):
    NO_ADOPTING_PROVIDERS = 'noad'
    AT_LEAST_1_ADOPTING_PROVIDER = 'al1ad'
    ALL_ADOPTING_PROVIDERS = 'allad'
    
class TopologySection(Enum):
    EDGE = 'edge'
    ETC = 'etc'
    INPUT_CLIQUE = 'clique'
    ALL= 'all'

class Outcomes(Enum):
    HIJACKED = 'hijacked'
    VICTIM_SUCCESS = 'successful'
    DISCONNECTED = 'disconnected'
    
def get_column_name(
        adopting,
        provider_setting,
        using_adopting_provider,
        topology_section,
        outcome
    ):
    adoption_setting = 'ad' if adopting else 'nonad'
    using_adopting_provider_setting = 'using' if using_adopting_provider else 'notusing'
    return '_'.join([adoption_setting, provider_setting.value,
                     using_adopting_provider_setting, topology_section.value, outcome.value])

def convert_data_as_fraction(adopting=True,
                             provider_setting=ProviderSetting.ALL_ADOPTING_PROVIDERS,
                             topology_section=TopologySection.EDGE,
                             outcome=Outcomes.VICTIM_SUCCESS):
    total = None
    feature_total = None
    for outcome_i in (Outcomes.VICTIM_SUCCESS, Outcomes.HIJACKED, Outcomes.DISCONNECTED):
        for using_adopting_provider_setting in (True, False):
            feature = get_column_name(
                          adopting,
                          provider_setting,
                          using_adopting_provider_setting,
                          topology_section,
                          outcome_i
                      )
            # Total for the selected outcome
            if outcome_i == outcome:
                if feature_total is not None:
                    feature_total = feature_total + data[feature].fillna(0)
                else:
                    feature_total = data[feature].fillna(0)
            # Total for all outcomes
            if total is not None:
                total = total + data[feature].fillna(0)
            else:
                total = data[feature].fillna(0)
    
    # Create new feature name
    # Remove the using_adopting_provider_setting attribute of name
    result_feature_new_name = get_column_name(
                                  adopting,
                                  provider_setting,
                                  using_adopting_provider_setting,
                                  topology_section,
                                  outcome
                             ).replace('_notusing', '').replace('_using', '')
    
    # Compute new feature fraction
    data[result_feature_new_name] = feature_total / total
    
    # Return name of new feature
    return result_feature_new_name
    
    # if outcome == Outcomes.VICTIM_SUCCESS:
    #     data[result_feature_new_name] = data[successful_feature] / total
    #     return result_feature_new_name
    # elif outcome == Outcomes.HIJACKED:
    #     data[hijacked_feature] = data[hijacked_feature] / total
    #     return hijacked_feature
    # elif outcome == Outcomes.DISCONNECTED:
    #     data[disconnected_feature] = data[disconnected_feature] / total
    #     return disconnected_feature
    # else:
    #     raise f"Unknown outcome specified: {outcome}"
    
    # if topology_section == TopologySection.EDGE:
    #     return  data[column_name] / (dm.num_stubs_of_multihomed_ases * data['percentage'])
    # elif topology_section == TopologySection.ETC:
    #     return  data[column_name] / (dm.num_etc_ases * data['percentage'])
    # elif topology_section == TopologySection.INPUT_CLIQUE:
    #     return  data[column_name] / (dm.num_input_clique_ases * data['percentage'])
    # elif topology_section == TopologySection.ALL:
    #     return  data[column_name] / (dm.num_all_ases * data['percentage'])
    # else:
    #     raise f"Unknown TopologySection specified: {topology_section}"
    
    
#%%-----------------------------
# Aggregate
#-------------------------------

data['noad_allad_notusing_edge_successful'] = np.nan

# Select Columns
#---------------------------
# Adopting ASes
# EDGE
# VICTIM SUCCESS
#---------------------------

# All Adopting Providers
adopting_all_providers = convert_data_as_fraction(
        adopting=False,
        provider_setting=ProviderSetting.ALL_ADOPTING_PROVIDERS,
        topology_section=TopologySection.EDGE,
        outcome=Outcomes.DISCONNECTED
    )

# At least 1 adopting provider
adopting_al1ad_providers = convert_data_as_fraction(
        adopting=False,
        provider_setting=ProviderSetting.AT_LEAST_1_ADOPTING_PROVIDER,
        topology_section=TopologySection.EDGE,
        outcome=Outcomes.DISCONNECTED
    )

# No adopting providers
adopting_no_providers = convert_data_as_fraction(
        adopting=False,
        provider_setting=ProviderSetting.NO_ADOPTING_PROVIDERS,
        topology_section=TopologySection.EDGE,
        outcome=Outcomes.DISCONNECTED
    )HIJACKED


#%% Perform the aggregation
data_agg = data.groupby(['percentage', 'propagation_round', 'adoption_setting']).agg({adopting_all_providers: 'mean',
                                                                                      adopting_al1ad_providers: 'mean',
                                                                                      adopting_no_providers: 'mean'}).reset_index()
data_agg.columns = list(map(''.join, data_agg.columns.values))

#%%
melted_data_agg = pd.melt(data_agg,
                          id_vars=['percentage', 'propagation_round', 'adoption_setting'])


#%%#############################
# Plotting
################################

px.line(melted_data_agg, x='percentage', y='value', color='variable', markers='.')



