#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:57:14 2023

@author: Reynaldo Morillo
"""

import json
from v4_graph_generator import PolicyResult, Line, generate_plot


paths = []
cdns = ["akamai", "cloudflare", "verisign", "incapsula", "neustar"]
lines_map = dict()
for i, cdn in enumerate(cdns):
    paths.append(f"../../data/graphs/jsons/artemis_{cdn}_cdn_5_attacker_50_trials.json")
    lines_map[i] = f"ARTEMIS {cdn.capitalize()} - 5 Attackers"

results = []
for path in paths:
    json_data = []
    with open(path, "r") as json_file:
        json_data.append(json.load(json_file))
        result = PolicyResult(
            "v4_victim_success_all", "0", "BGP Simple", "ARTEMIS", json_data
        )
        results.append(result)

lines = []
for i, result in enumerate(results):
    lines.append(
        Line(lines_map[i], False, result.non_adopting["v4_victim_success_all"])
    )


generate_plot(
    lines,
    ylim=100,
    outcome_text="Attacker Success",
    size_inches=(5, 4),
    legend_kwargs={"loc": "upper left", "prop": {"size": 11}},
    fname="./plots/artemis-5-attackers-victim-success.pdf",
)
