import sys
import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from textwrap import wrap
from math import sqrt
from enum import Enum
import json
from copy import deepcopy

from statistics import mean, stdev

# Colors and styles should be consistent!

bgpsec_color = 'C1' # purple
bgpisec_color = 'C2' # green
path_end_color = 'C0' # blue
baseline_color = 'C7' # grey

bgpsec_style = 'dashed'
default_style = 'solid'
path_end_style = 'dotted'

default_marker = ''
overhead_marker = 'P'
aggressive_marker = '*'
timid_marker = '.'
baseline_marker = ''


linemap = {
    'BGP': {'color': baseline_color, 'marker': baseline_marker, 'linestyle': default_style},
    'BGP+100% ROV': {'color': baseline_color, 'marker': '', 'linestyle': default_style},
    'BGPsec': {'color': bgpsec_color, 'marker': aggressive_marker, 'linestyle': bgpsec_style},
    'BGPsec+100% ROV': {'color': bgpsec_color, 'marker': aggressive_marker, 'linestyle': bgpsec_style},
    'BGPsec, No Attack': {'color': bgpsec_color, 'marker': overhead_marker, 'linestyle': bgpsec_style},
    'BGP-iSec, No Attack': {'color': bgpisec_color, 'marker': overhead_marker, 'linestyle': default_style},
    'BGPsec, Aggressive': {'color': bgpsec_color, 'marker': aggressive_marker, 'linestyle': bgpsec_style},
    'Path End, 2-hop': {'color': path_end_color, 'marker': aggressive_marker, 'linestyle': path_end_style},
    "BGP-iSec-Trans-DO only": {'color': 'C4', 'marker': timid_marker, 'linestyle': 'dotted'},
    "BGP-iSec-Trans-DO only, Aggressive": {'color': 'C4', 'marker': aggressive_marker, 'linestyle': 'dotted'},
    "BGP-iSec-Trans-DO only, Timid": {'color': 'C4', 'marker': timid_marker, 'linestyle': 'dotted'},
    "BGP-iSec-Trans-DO only, Connector": {'color': 'C4', 'marker': '', 'linestyle': 'dotted'},
    'BGP-iSec+100% ROV, Aggressive': {'color': bgpisec_color, 'marker': aggressive_marker, 'linestyle': default_style},
    'BGP-iSec+100% ROV, Timid': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': default_style},
    'BGP-iSec+100% ROV, Timid-Path': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': default_style},
    'BGP-iSec+100% ROV, Connector': {'color': bgpisec_color, 'marker': '', 'linestyle': default_style},
    'BGP-iSec': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': default_style},
    'BGP-iSec, Aggressive': {'color': bgpisec_color, 'marker': aggressive_marker, 'linestyle': default_style},
    'BGP-iSec, Timid': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': default_style},
    'BGP-iSec No Encrypted UP, Timid-Path No Eavesdropping': {'color': 'C7', 'marker': timid_marker, 'linestyle': 'dashed'},
    'BGP-iSec No Encrypted UP, Timid-Path Eavesdropper': {'color': 'C8', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec Encrypted UP, Timid-Path Eavesdropper': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': 'solid'},
    'Path End': {'color': path_end_color, 'marker': timid_marker, 'linestyle':  path_end_style},
    'Path End, Aggressive': {'color': path_end_color, 'marker': aggressive_marker, 'linestyle':  path_end_style},
    'Path End, Connector': {'color': path_end_color, 'marker': '', 'linestyle':  path_end_style},
    'BGP-iSec Trans, Timid-Path': {'color': 'C8', 'marker': timid_marker, 'linestyle': 'dashed'},
    'BGP-iSec Transitive Only': {'color': 'C8', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec Transitive Only, Timid': {'color': 'C8', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec Transitive Only, Aggressive': {'color': 'C8', 'marker': aggressive_marker, 'linestyle': 'dotted'},
    'BGP-iSec Transitive Only, Connector': {'color': 'C8', 'marker': '', 'linestyle': 'dotted'},
    'BGP-iSec, Timid-All': {'color': 'C9', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec, Timid-Path': {'color': bgpisec_color, 'marker': timid_marker, 'linestyle': 'dashed'},
    'BGP-iSec, Connector': {'color': bgpisec_color, 'marker': '', 'linestyle': default_style},
    'BGP-iSec Trans-DO, Timid-Path': {'color': 'C7', 'marker': timid_marker, 'linestyle': 'dashed'},
    'BGP-iSec with Path Shortening Defense': {'color': 'C7', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec with Path Shortening Defense, Aggressive': {'color': 'C7', 'marker': aggressive_marker, 'linestyle': 'dotted'},
    'BGP-iSec with Path Shortening Defense, Timid': {'color': 'C7', 'marker': timid_marker, 'linestyle': 'dotted'},
    'BGP-iSec with Path Shortening Defense, Connector': {'color': 'C7', 'marker': '', 'linestyle': 'dotted'},
    # the transitive dropping part is incoherent with the rest
    'No Transitive Dropping': {'color': 'C7', 'marker': '.', 'linestyle': 'solid'},
    '1% Transitive Dropping': {'color': 'C8', 'marker': '.', 'linestyle': 'dotted'},
    '2% Transitive Dropping': {'color': 'C9', 'marker': '.', 'linestyle': 'dashed'},
    '4% Transitive Dropping': {'color': 'C6', 'marker': '.', 'linestyle': 'dashdot'},
    '8% Transitive Dropping': {'color': 'C5', 'marker': '.', 'linestyle': 'dotted'},
    '16% Transitive Dropping': {'color': 'C4', 'marker': '.', 'linestyle': 'dotted'},
    '32% Transitive Dropping': {'color': 'C3', 'marker': '.', 'linestyle': 'dotted'},
    '64% Transitive Dropping': {'color': 'C2', 'marker': '.', 'linestyle': 'dotted'},
    '99% Transitive Dropping': {'color': 'C6', 'marker': '.', 'linestyle': 'dotted'},
    'BGP-iSec, Timid Overhead 99% dropping': {'color': 'C6', 'marker': overhead_marker, 'linestyle': 'dotted'},
}

class Line:
    """Formats raw data for matplotlib graph"""

    def __init__(self, scenario_label, has_connector: bool, percent_adopt_dict):
        """Stores info aobut a line in a graph"""

        # {percent_adopt: [percentages]}
        self.percent_adopt_dict = percent_adopt_dict
        self.label = scenario_label
        self.x = self._get_x()
        self.y = self._get_y()
        self.yerr = self._get_yerrs()
        self.has_connector: bool = has_connector

    def _get_x(self):
        """"Gets X axis makers"""

        return list(self.percent_adopt_dict)

    def _get_y(self):
        """Gets Y axis markers"""

        return [mean(x) for x in self.percent_adopt_dict.values()]
    
    def _get_scaled_y(self):
        """Gets Y axis markers"""

        _mean = mean(self._get_y())
        return [_mean] * len(self.percent_adopt_dict)

    def _get_yerrs(self):
        """Gets Yerr for each data point"""

        return [self._get_yerr(x) for x in self.percent_adopt_dict.values()]

    def _get_yerr(self, list_of_vals):
        """Gets yerr for a single list of values, 90% confidence"""

        if len(list_of_vals) > 1:
            yerr_num = 1.645 * 2 * stdev(list_of_vals)
            yerr_denom = sqrt(len(list_of_vals))
            return yerr_num / yerr_denom
        else:
            return 0

def scale_line(bgp_line, other_line):
    avg_bgp = bgp_line._get_scaled_y()
    for i in range(len(bgp_line.y)):
        ratio = avg_bgp[i] / bgp_line.y[i]
        # scale values to avg_bgp
        other_line.y[i] *= ratio

class ASType(Enum):
    ETC = ("etc", "etc")
    INPUT_CLIQUE = ("input_clique", "input_clique_subgraph")
    STUBS_MULTIHOME = ("stubs_and_multihomed", "stubs_and_multihomed")

class PolicyResult:
    def __init__(self, subgraph_name: str, propagation_round: int, base_policy_name: str, adopting_policy_name: str, json_data):
        def parse(subgraph_name: str):
            result: {ASType: {int, [float]}} = {}
            temp: {ASType: [(int, [float])]} = {}

            for dataset in json_data:
                rates = dataset[subgraph_name][propagation_round][f"{base_policy_name} ({adopting_policy_name} adopting)"]
                for adoption_rate, success_rates in rates.items():
                    if subgraph_name not in temp:
                        temp[subgraph_name] = [(float(adoption_rate), success_rates)]
                    else:
                        temp[subgraph_name].append((float(adoption_rate), success_rates))

            # json does not guarantee order
            for subgraph_name, rates in temp.items():
                rates.sort(key=lambda y: y[0])
                temp_dict: {float, [float]} = {}
                for (adopt_rate, success) in rates:
                    if adopt_rate not in temp_dict:
                        temp_dict[adopt_rate] = success
                    else:
                        temp_dict[adopt_rate] += success
                result[subgraph_name] = temp_dict

            return result

        # self.adopting = parse(adopting_name_prefix, 0)
        self.non_adopting = parse(subgraph_name)


def generate_plot(lines: [Line], 
                 outcome="Attacker Success",
                 order=None,
                 size_inches=None,
                 legend_kwargs=None,
                 fname=None,
                 drop_columns=None,
                 text_replaces=None,
                 textwidth=30,
                 outcome_text=None,
                 ylim=None):
    fig, ax = plt.subplots()
    #plt.xlim(0, 1.3)
    
    ylim = 32 if ylim is None else ylim
    plt.ylim(0, ylim)

    plt.xticks([int(x*100) for x in lines[0]._get_x()])

    used_labels = set()

    for line in lines:
        ax.errorbar([x*100 for x in line._get_x()],
                    line.y,
                    yerr=line.yerr,
                    linestyle=linemap[line.label]['linestyle'],# if not line.has_connector else 'None',
                    label="" if (line.label in used_labels) else line.label,
                    color=linemap[line.label]['color'],
                    marker=linemap[line.label]["marker"],
                    path_effects=[path_effects.SimpleLineShadow(offset=(0, -0.5)), path_effects.Normal()])

        used_labels.add(line.label)

    if outcome_text is None:
        outcome_text = "Attacker Success"
    ax.set_ylabel(f"{outcome_text}")
    ax.set_xlabel("Percent adoption")

    # Might throw warnings later?
    # redundant?
    # legend = plt.legend()
    # print(legend.get_texts()) #[0].set_text('make it short')
    plt.tight_layout()
    plt.rcParams.update({"font.size": 14, "lines.markersize": 10})
    #matplotlib.use('Agg')

    # Anchor legend to right of graph
    if legend_kwargs is None:
        legend_kwargs = {'bbox_to_anchor': (1.05, 0.75, 0.3, 0.2), 'loc': 'upper left'}
    if order is not None:
        handles, labels = plt.gca().get_legend_handles_labels()
        # Text replaces
        if text_replaces is not None:
            for i, text in enumerate(labels):
                for tr in text_replaces:
                    labels[i] = labels[i].replace(tr[0], tr[1])
        labels = ['\n'.join(wrap(l, textwidth)) for l in labels]
        legend = plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order], **legend_kwargs)
    else:
        legend = plt.legend(**legend_kwargs)
        # Text replaces
        if text_replaces is not None:
            for text in legend.get_texts():
                for tr in text_replaces:
                    text.set_text(text.get_text().replace(tr[0], tr[1]))
        handles, labels = plt.gca().get_legend_handles_labels()
        labels = ['\n'.join(wrap(l, textwidth)) for l in labels]
        legend = plt.legend(handles, labels, **legend_kwargs)

    # horizontal grid lines
    plt.gca().yaxis.grid()
    fig.set_dpi(150)
    if size_inches is None:
        fig.set_size_inches(9, 6, forward=True)
    else:
        fig.set_size_inches(*size_inches, forward=True)
    
    plt.xlim(0, 100)
    if fname is not None:
        plt.savefig(fname, bbox_inches='tight')
    else:
        plt.show()

def optimal_line(scenario_label, lines: [Line], invert=False):
    """If scaling, lines should be scaled before calling this"""
    if len(lines) == 0:
        return None

    lines_to_ret: [Line] = []

    adopt_dict: {int, [float]} = {}
    policy: str = lines[0].label
    
    lines_to_ret.append(Line(scenario_label, False, deepcopy(adopt_dict))) # connector
    for line in lines:
        lines_to_ret.append(Line(line.label, True, deepcopy(adopt_dict)))
    
    for i in range(len(lines[0].x)):
        adoption_rate = lines[0].x[i]

        optimal_ys = lines[0].percent_adopt_dict[adoption_rate]
        optimal_policy = lines[0].label

        for j in range(len(lines)):
            if invert:
                if lines[j].y[i] < mean(optimal_ys):
                    optimal_ys = lines[j].percent_adopt_dict[adoption_rate]
                    optimal_policy = lines[j].label
            else:
                if lines[j].y[i] > mean(optimal_ys):
                    optimal_ys = lines[j].percent_adopt_dict[adoption_rate]
                    optimal_policy = lines[j].label

        for line in lines_to_ret:
            if line.label == optimal_policy:
                line.percent_adopt_dict[adoption_rate] = optimal_ys
        lines_to_ret[0].percent_adopt_dict[adoption_rate] = optimal_ys
        
    for line in lines_to_ret:
        line.x = line._get_x()
        line.y = line._get_y()
        line.yerr = line._get_yerrs()
    return lines_to_ret
