#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:54:52 2022

@author: reynaldo
"""

import pandas as pd
import numpy as np
import ast



#################################
# Load the data
#################################

# project_path = '/home/reynaldo/Dropbox/School/Research/BGP/ROV++/projects/secure_monitoring_service_pkg/secure_monitoring_service_pkg/analysis'
# avoid_list_path = './report_path_lists/avoid_list_5_trails_brackets_removed.tsv'
# as_metadata_path = './as_metadata/head_80000_k0_5_trials_as_metadata_brackets_removed.tsv'
avoid_list_path = './report_path_lists/avoid_list_1_trails.tsv'
as_metadata_path = './as_metadata/k0_1_trials_as_metadata.tsv'

avoid_lists = pd.read_csv(avoid_list_path, sep='\t', header=0)
as_metadata = pd.read_csv(as_metadata_path, sep='\t', header=0)

avoid_lists.set_index(['percentAdoption', 'trial'])
as_metadata.set_index(['percentAdoption', 'trial'])

# Preprocess the data
merged_data = avoid_lists.merge(as_metadata)

#merged_data['avoidList'] = merged_data.avoidList.apply(lambda x: x.strip('[]').split(', '))
merged_data['avoidList'] = merged_data.avoidList.apply(lambda s: set(ast.literal_eval(s) if pd.notnull(s) else set([0])))
merged_data['legitPrefixASPath'] = merged_data.legitPrefixASPath.apply(lambda s: set(ast.literal_eval(s)) if  pd.notnull(s) else set([0]))

merged_data['intersection'] = merged_data.apply(lambda x: x.avoidList.intersection(x.legitPrefixASPath) if pd.notnull(x.avoidList) and pd.notnull(x.legitPrefixASPath) else np.nan, axis=1)
#merged_data['intersection'] = merged_data.legitPrefixASPath.apply(lambda s: list(s) if pd.notnull(s) else s)

# Save to file

all_the_things = list()
for inter in merged_data['intersection']:
    for x in inter:
        all_the_things.append(x)

output_df = pd.DataFrame({'triggerASes': all_the_things})
output_df.to_csv('triggerASes.tsv', sep='\t')
