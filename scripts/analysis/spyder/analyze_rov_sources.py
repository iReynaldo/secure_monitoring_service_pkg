#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:46:35 2023

@author: uconn
"""


# %%############################
# Imports
################################


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import plotly.io as pio

import data_manager as dm

# %%############################
# Load Data
################################

# Configure plotting
pio.renderers.default = "browser"

# Load Data from CSVs
data_file_path = "../../../secure_monitoring_service_pkg/aux_files/rov_adoption_real.csv"
data = pd.read_csv(data_file_path, delimiter=",")


# %%############################
# Preprocessing
################################ 

apnic = data.loc[data['source'] == 'APNIC', ]
rovista = data.loc[data['source'] == 'ROVISTA', ]

df = pd.merge(apnic, rovista, on='asn', how='inner')


# %%############################
# Plotting
################################ 

_fig = plt.figure()

# Making an axis instance
_ax = _fig.add_axes([0, 0, 1, 1])
plt.rcParams.update({"font.size": 21, "lines.markersize": 8})

plt.scatter(df.confidence_x * 100, df.confidence_y * 100, alpha=0.5)

# Set Y and X axis Labels
_ax.set_xlabel("APNIC Score (%)")
_ax.set_ylabel("RoVista Score (%)")
# _ax.legend(loc="best")
_ax.axline([0, 0], [100, 100], linestyle='dashed', color='black', alpha=1)

# Other plot settings
_fig.set_dpi(150)
_fig.set_size_inches(5, 4, forward=True)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.gca().yaxis.grid()
plt.tight_layout()

# matplotlib.rcParams.update({'font.size': 22})


plt.savefig(
    "./minerva_plots/others/apnic_rovista_conf_diff.pdf",
    bbox_inches="tight",
)