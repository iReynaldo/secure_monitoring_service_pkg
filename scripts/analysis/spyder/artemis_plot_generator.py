#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:57:14 2023

@author: Reynaldo Morillo
"""

# import pandas as pd

# with open('../../data/graphs/jsons/artemis_verisign_cdn_1_attacker_50_trials.json', encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile)


# df.to_csv('csvfile.csv', encoding='utf-8', index=False)

import json
from v4_graph_generator import PolicyResult, Line, generate_plot


for cdn in ["akamai", "cloudflare", "verisign", "incapsula", "neustar"]:
    paths = []
    for num_attackers in [1, 2, 5]:
        paths.append(
            f"../../data/graphs/jsons/artemis_{cdn}_cdn_{num_attackers}_attacker_50_trials.json"
        )

    results = []
    for path in paths:
        json_data = []
        with open(path, "r") as json_file:
            json_data.append(json.load(json_file))
            result = PolicyResult(
                "v4_disconnected_all", "0", "BGP Simple", "ARTEMIS", json_data
            )
            results.append(result)

    lines = []
    capitalized_cdn = cdn.capitalize()
    lines_map = {
        0: f"ARTEMIS {capitalized_cdn} - 1 Attackers",
        1: f"ARTEMIS {capitalized_cdn} - 2 Attackers",
        2: f"ARTEMIS {capitalized_cdn} - 5 Attackers",
    }

    for i, result in enumerate(results):
        lines.append(
            Line(lines_map[i], False, result.non_adopting["v4_disconnected_all"])
        )

    generate_plot(
        lines,
        ylim=100,
        outcome_text="Attacker Success",
        size_inches=(5, 4),
        legend_kwargs={"loc": "upper left", "prop": {"size": 11}},
        fname=f"./plots/artemis-{cdn}-disconnected.pdf",
    )
