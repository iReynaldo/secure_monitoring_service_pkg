#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:34:27 2023

@author: uconn
"""

# %%#############################
# Imports
################################


import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio

import data_manager as dm

# %%#############################
# Load Data
################################

# Configure plotting
pio.renderers.default = "browser"

# Data configuration
relay = "neustar"
rov_setting = "none"
num_trials = 8000
tunnel = True

# TODO: Future new files will need the Tunnel
# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = f"../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_{tunnel}_tunnel_{relay}_relay_False_attackRelay_1_attacker_{num_trials}_trials_full_percentages_avoid_list_metadata.csv"
data_not_attacked = pd.read_csv(data_file_path, delimiter="\t")

data_file_path_attacked = f"../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_{tunnel}_tunnel_{relay}_relay_True_attackRelay_1_attacker_{num_trials}_trials_full_percentages_avoid_list_metadata.csv"
data_attacked = pd.read_csv(data_file_path_attacked, delimiter="\t")


# %% Preview Data Columns
data_not_attacked.columns.to_list()

# %%#############################
# Preprocessing
################################

# Combine dataframes
data_not_attacked["attack_relay"] = False
data_attacked["attack_relay"] = True
data = pd.concat([data_not_attacked, data_attacked])


# %% Calculate Basic Stats on Avoid List Length
feature = "edge_using_relay"
# TODO: make if else ladder for different feature settings (edge, etc, clique)
data[feature] = data[feature] / (dm.num_stubs_of_multihomed_ases * data["percentage"])

# %%
relay_data_agg = (
    data.groupby(
        ["percentage", "propagation_round", "adoption_setting", "attack_relay"]
    )
    .agg({feature: ["mean", dm.calc_90_per_conf]})
    .reset_index()
)
relay_data_agg.columns = list(map("".join, relay_data_agg.columns.values))

# data_hist = data[feature].value_counts().plot.bar(rot=0)

# %%#############################
# Plotting
################################


# %% Plotly Line Plot
# fig = px.line(relay_data_agg, x='percentage', y=feature+'mean', color='attack_relay', markers='.')
# fig.show()


# %% Matplotlib Line Plot
_fig = plt.figure()

# Making an axis instance
_ax = _fig.add_axes([0, 0, 1, 1])

# Make Plot
colors = ("blue", "red")
labels = ("Relay Not Attacked", "Relay Attacked")
for i, attack_relay_setting in enumerate((False, True)):
    df = relay_data_agg[relay_data_agg.attack_relay == attack_relay_setting]
    _ax.errorbar(
        df.percentage * 100,
        df[feature + "mean"] * 100,
        yerr=df[feature + "calc_90_per_conf"] * 100,
        marker=".",
        color=colors[i],
        label=labels[i],
    )
# _ax.plot(x=relay_data_agg.loc[relay_data_agg['attack_relay']==False,'percentage'], y=relay_data_agg[relay_data_agg['attack_relay']==False, feature+'mean'], color='blue')
# _ax.plot(relay_data_agg['percentage'], relay_data_agg[feature+'mean'], color='red')
# _ax.plot(relay_data_agg['percentage'], relay_data_agg[feature+'mean'], color='red')

# Set Y and X axis Labels
_ax.set_ylabel("Percent of edge ASes using relays")
_ax.set_xlabel("Percent adoption")
_ax.legend(loc="best")


_fig.set_dpi(150)
_fig.set_size_inches(5, 4, forward=True)
plt.xlim(0, 100)
plt.gca().yaxis.grid()
plt.tight_layout()
plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
plt.savefig(
    f"./immunity_paper_plots/pheme/subprefix/rov_{rov_setting}/relay_usage_{relay}.pdf",
    bbox_inches="tight",
)


# We look at relay usage because it explains why the attack relay setting has almost no effect on the
# the performance of the policies. The attack relay objective is aimed to impact the reachability
# of the relays from the users of the relays, rather than to impact the relays themselves.
# Looking at relay usage we can see how the access to the relays have been impacted by the
# prefix attack launched on them. Observing the results of a prefix hijack we can approximate the
# affect of these types of attacks are not very effective for our policies. Hence the relative
# small impact it has on relay usage. Moreover, from this we can see that a relatively
# small percentage of the adopting ASes rely on the relays, with at most 17.5% of them around 40-60%
# adoption. It's around this area we can see a more distinguishable difference in the attack relay
# results, albiet small; which corresponds with the relative difference in relays usage of about 1%
# due to the impact of the relay attack.
