#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16, 2023

@author: Reynaldo Morillo
"""

from collections import defaultdict
from statistics import mean

import pandas as pd

from v4_graph_generator import Line
import data_manager as dm


####################################
# Main
####################################

# Example file name
# V4SubprefixHijackScenario_scenario_none_type_others_policies_real_rov_0_hash_False_probe_twenty_relay_False_attackRelay_1_attacker_2000_trials_full_percentages

# -----------------------------------
# Constants
# -----------------------------------


# -----------------------------------
# Args
# -----------------------------------

scenario = "V4SubprefixHijackScenario"
scenario_type = "none"
simulated_policies = "others"  # standard
# rov_setting = 'real'
rov_setting = "none"
hash_seed = 0
probe = False
# relay
attack_relay = False
num_attackers = 1
num_trials = 2000

metric = dm.victim_success
# relays = ['akamai', 'cloudflare', 'verisign', 'incapsula', 'neustar', 'conglomerate']
relays = ["five", "ten", "twenty", "forty"]
policy = "rovppo"
# policy = 'v4'

# Save measurements for tab
data_table = defaultdict(list)
data_table["relays"] = relays

for metric in [dm.attacker_success, dm.victim_success, dm.disconnections]:
    # Load paths
    paths = list()
    for relay in relays:
        paths.append(
            dm.json_file(
                scenario,
                scenario_type,
                simulated_policies,
                rov_setting,
                hash_seed,
                probe,
                relay,
                attack_relay,
                num_attackers,
                num_trials,
            )
        )

    # Load Results
    subgraph = dm.metric_subgraph[metric]
    results = dm.get_results(paths, subgraph, [dm.policy_name_map[policy]])

    # Generate Lines
    line_styles_map = dict()
    for i, relay in enumerate(relays):
        line_styles_map[i] = dm.lines_style_mapper(policy, relay)

    # Extract percentage data for metric
    for i, result in enumerate(results):
        if result:
            new_line = Line(line_styles_map[i], False, result.adopting[subgraph])
            data_table[metric].append(mean(new_line.y))
        else:
            data_table[metric].append(None)


# Calculate special score
# successful_connections - (disconnections + attacker_success)
scores = list()
for i in range(len(relays)):
    if (
        data_table[dm.victim_success][i]
        and data_table[dm.attacker_success][i]
        and data_table[dm.disconnections][i]
    ):
        scores.append(
            data_table[dm.victim_success][i]
            - (data_table[dm.attacker_success][i] + data_table[dm.disconnections][i])
        )
    else:
        scores.append(None)

# Add other columns
data_table["scores"] = scores

# Create final dataframe
table = pd.DataFrame(data=data_table)

# Latex table formatting details
# Sort Dataframe by Score (Descending)
table.sort_values(by="scores")
# Round the floats to 4 or 5 decimal places
table.round(decimals=4)
# TODO: Capitalize names of columns and relays
# TODO: Try truncating the column names (for space)


# Set which policy directory the result is saved too
policy_dir = "immunity" if policy == "rovppo" else "pheme"
# Set overlay type
relay_filename = "cdns" if relays[0] in dm.cdns else "peers"

fname = f"./immunity_paper_plots/{policy_dir}/subprefix/rov_{rov_setting}/subprefix_{relay_filename}_relay.csv"

table.to_csv(
    fname,
    index=False,
)
