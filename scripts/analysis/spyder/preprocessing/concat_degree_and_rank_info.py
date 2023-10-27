#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:20:11 2023

@author: uconn
"""
import sys
import pandas as pd


###########################
# Constants
###########################

# Auxiliary data (i.e. AS degree and rank information)
AUX_DATA_FILE_PATH = './asn_degree_and_rank.csv'

###########################
# Arguments
###########################
#%%

main_data_file_path = sys.argv[1]
# Output filename
output_filename = main_data_file_path.split('.')[0] + '_augmented.csv'

###########################
# Load Data
###########################
#%%

main_data = pd.read_csv(main_data_file_path, delimiter='\t')
aux_data = pd.read_csv(AUX_DATA_FILE_PATH, delimiter='\t')

###########################
# Preprocessing
###########################
#%%

###########################
# Main
###########################
#%%

print(f"Merging: {main_data_file_path}")
merged_data = pd.merge(main_data, aux_data, how='left', on='asn')
print(f"Writing file: {output_filename}")
merged_data.to_csv(output_filename, sep='\t')
