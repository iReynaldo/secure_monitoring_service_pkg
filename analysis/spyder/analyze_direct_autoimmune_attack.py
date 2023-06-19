#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:59:10 2023

@author: uconn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


################################
# Load Data
################################
#%%
data_file_path = '../../data/as_metadata/metadata.csv'
data = pd.read_csv(data_file_path, delimiter='\t')



################################
# Functions
################################

def clean_alt_list(list_):
    list_ = list_.replace(', ', '","')
    list_ = list_.replace('[', '["')
    list_ = list_.replace(']', '"]')
    return list_

################################
# Preprocess
################################
#%%

# Analyze the size of the avoid list
unique_avoid_lists = data.loc[:, 'avoid_list'].unique()
# The avoid list of each one is just a single AS ... this is true for every pecentage value I checked ...
# This must be true because the Direct AutoImmune attack targets a single provider of the origin. Therefore, 
# the avoid list would have at most one ASN in it for this attack for the given attacking subprefix.
# Some ASes don't have that ASN in its avoid list most likely because the origin is a multihomed AS; which means
# the adopting ASes that have a successful connection to the origin are connected via the path of the other provider
# of the multihomed origin.
# From here we need to check what fraction of edge ASes are multihomed
# Computer the following ==== Fraction of edge ASes that are multihomed: 0.5655785325105595

# Convert list data values (which are default interpreted as strings) to list data types
data['as_path'] = data['as_path'].apply(eval)
data['avoid_list'] = data['avoid_list'].apply(eval)

################################
# Analyze
################################
#%%

# Count the disconnected in a single trial (adopting)
adopting_ases_trials = data.loc[data['adoption_setting'] == 'ROV V4 Lite K2', :]
disconnected_adopting_ases_trials = adopting_ases_trials.loc[adopting_ases_trials['outcome'] == 'Outcomes.DISCONNECTED', :]
successful_adopting_ases_trials = adopting_ases_trials.loc[adopting_ases_trials['outcome'] == 'Outcomes.VICTIM_SUCCESS', :]


sinlge_trial_data = disconnected_adopting_ases_trials.loc[(disconnected_adopting_ases_trials['trial'] == 1) & (disconnected_adopting_ases_trials['percentage'] == 0.4), :]
successful_single_trial_data = successful_adopting_ases_trials.loc[(successful_adopting_ases_trials['trial'] == 1) & (successful_adopting_ases_trials['percentage'] == 0.4), :]

ten_percent_trials = adopting_ases_trials.loc[adopting_ases_trials['percentage'] == 0.1, :]

# Check the fraction of disconnected / all_ases (should be close to 80% according to the phenomenon we're investigating)
print(len(disconnected_adopting_ases_trials)/len(adopting_ases_trials))
print(len(successful_adopting_ases_trials)/len(adopting_ases_trials))

#%%
# The following is a bad idea .... tooo many ASes in the count
# Create a histogram of the ASes that are disconnected, and see if there's some consistency with their disconnections
# fig, ax = plt.subplots() 
# adopting_ases_trials['asn'].value_counts().plot(kind='bar')
counts = ten_percent_trials['asn'].value_counts()

#%%
# Check the contents of their RIBs
## Do they have a blackhole?
## Do they have a path to the origin without a blackhole?
single_trial_prefix_outcome = sinlge_trial_data.loc[sinlge_trial_data['prefix_for_outcome'] == sinlge_trial_data['local_rib_prefix'], :]
disconnected_ases_with_blackhole = sum(single_trial_prefix_outcome['blackhole'] == True)
# Fraction of ASes that are disconnected due to blackhole -- It should be all of them -- it is ...
print(disconnected_ases_with_blackhole/len(single_trial_prefix_outcome['asn'].unique()))

# Lets check the RIB of those who are successfully connected. How is it possible?
# Did they not install a blackhole? For what reason?
successful_single_trial_data_prefix_outcome = successful_single_trial_data.loc[successful_single_trial_data['prefix_for_outcome'] == successful_single_trial_data['local_rib_prefix'], :]
# It seems that those who are successfully connected do not have a path to the prefix choosen for the outcome.
# That's of course true, because this is a direct autoimmune attack (i.e. there is no actual announcement)
print(len(successful_single_trial_data_prefix_outcome))

# Check if any of the successfully connected have a member of the avoid list in there path
avoid_list_item_in_success_path = successful_single_trial_data.apply(lambda row: any(asn in row.as_path for asn in row.avoid_list), axis=1)
print(any(avoid_list_item_in_success_path))

#%%



################################
# Graph
################################
#%%