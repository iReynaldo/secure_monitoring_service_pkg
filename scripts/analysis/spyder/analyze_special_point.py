#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:20:34 2023

@author: uconn
"""

# %%#############################
# Imports
################################


import pandas as pd
import plotly.io as pio


# %%#############################
# Load Data
################################

# Configure plotting
pio.renderers.default = "browser"

# Parameter
bgp_immunity_policy = "v4"  # 'rovppo'

# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = "../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_none_rov_0_hash_False_probe_True_tunnel_neustar_relay_False_attackRelay_1_attacker_16000_trials_[0.99]_percentages_as_metadata.csv"
data = pd.read_csv(data_file_path, delimiter="\t")


# %%#############################
# Preprocessing
################################

# Create empty_rib column
data["empty_rib"] = data.as_local_rib == "{}"
data["adopting"] = data.policy != "BGP Simple"

# %% Aggregate
data_agg = (
    data.groupby(["percentage", "propagation_round", "adoption_setting", "adopting"])
    .agg({"num_providers": "mean", "empty_rib": "mean"})
    .reset_index()
)
data_agg.columns = list(map("".join, data_agg.columns.values))

# %%  Determine Fraction

for policy in ("ROV V4 Lite", "ROV++ V1 Lite Simple Overlayed"):
    for adopting in (True, False):
        df = data[(data.adoption_setting == policy) & (data.adopting == adopting)]
        print(f"{policy} Adopting = {adopting}")
        # Fraction of ASes with empty RIB
        print(
            f"Fraction of ASes with empty Local-RIB: {sum(df.empty_rib) / len(df.empty_rib)}"
        )
        # Fraction of ASes with no provider
        print(
            f"Fraction of ASes with no provider: {sum(df.num_providers == 0) / len(df.num_providers)}\n"
        )

# From the above we can see that almost all the cases consist of
# - 0 providers
# - Empty Local Ribs

# Note, for the incenetive anlaysis you are only showing plots
# for the Monitoring System policy

# This inquiry was spurred by the observation made in the incentive analysis
# at the 99% point of ASes that have no adopting providers.
# The succsssful connections drops drastically, and the disconnections increase
# drastically. It's clear that the successful connections are being converted into
# disconnections. This analysis attempts to understand why there's a dramatic
# increase in disconnections in this population. Upon closer analysis, it's observered
# that adopting ASes in this population that are disconnected 99.4% are disconnected due to
# having empty Local-RIBs; which maybe attributed to the fact that 99.1%
# do not have any providers. In the case of the non-adopting ASes
# 89.1% have empty ribs, and 99.1% of them don't have providers. The problem with this percentage
# point is the fact that it consequently consolates ASes that have no providers. Edge ASes
# such as these tend to be exlcusively connected via multiple peers; which due to their posture
# in the topology, causes them to be largely unreachable. This is evident by the
# fact that they have emtpy Local-RIBs. An empty Local-RIB indicates that not even
# the legit origin prefix has reached them; which implies their reachability under any
# circumstance is limited.
