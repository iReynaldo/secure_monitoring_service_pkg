#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 23:22:58 2024

@author: uconn
"""

#%%#############################
# Imports
################################

from statistics import mean, stdev

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px
import plotly.io as pio

import data_manager as dm

#%%#############################
# Load Data
################################

# Configure plotting
pio.renderers.default = 'browser'

# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = f'../../../secure_monitoring_service_pkg/aux_files/rov_adoption_real.csv'
data = pd.read_csv(data_file_path)



#%%#############################
# Preprocessing
################################

rovista = data[data.source == 'ROVISTA']
apnic = data[data.source == 'APNIC']


#%%#############################
# Plotting
#################################

fig, axs = plt.subplots()

# Cumulative distributions.
n_bins = 500
# n, bins, patches = axs.hist(rovista.confidence, n_bins, histtype='bar', cumulative=-1, orientation='horizontal', hatch='/', label='ROVISTA')
# n, bins, patches = axs.hist(apnic.confidence, n_bins, histtype='bar', cumulative=-1, orientation='horizontal', alpha=0.85, label='APNIC')

rovista_n, rovista_bins, patches = plt.hist(rovista.confidence, n_bins, histtype='step', cumulative=-1, orientation='horizontal', label='ROVISTA')
rovista_bins_mean = [0.5 * (rovista_bins[i] + rovista_bins[i+1]) for i in range(len(rovista_n))]
apnic_n, apnic_bins, patches = plt.hist(apnic.confidence, n_bins, histtype='step', cumulative=-1, orientation='horizontal', label='APNIC')
apnic_bins_mean = [0.5 * (apnic_bins[i] + apnic_bins[i+1]) for i in range(len(apnic_n))]

# Create Scatter Plot CDF
fig, axs = plt.subplots()
axs.scatter(rovista_n, rovista_bins_mean, label='ROVISTA')
axs.scatter(apnic_n, apnic_bins_mean, label='APNIC')

# Formatting
axs.set_xlabel("Index")
axs.set_ylabel("Score")
axs.legend(loc='best')


fig.set_dpi(150)

fig.set_size_inches(5, 4, forward=True)
ylim = 100
plt.gca().yaxis.grid()
# plt.gca().xaxis.grid()
plt.tight_layout()
plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
plt.savefig(f"./minerva_plots/others/all_rov_confidence_distribution_new.pdf", bbox_inches='tight')
