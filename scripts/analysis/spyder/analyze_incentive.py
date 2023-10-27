#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:23:56 2023

@author: uconn
"""

# %%#############################
# Imports
################################

from collections import Counter
from math import sqrt
from statistics import mean, stdev
from enum import Enum

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

import data_manager as dm

# %%#############################
# Load Data
################################

# Configure plotting
pio.renderers.default = "browser"

# Parameter
bgp_immunity_policy = "v4"  # 'rovppo'

# Data configuration
relay = "neustar"
rov_setting = "none"
num_trials = 8000
tunneled = True

# TODO: Create a function to read the files into dataframes
# Load data
data_file_path = f"../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_{rov_setting}_rov_0_hash_False_probe_{tunneled}_tunnel_{relay}_relay_False_attackRelay_1_attacker_{num_trials}_trials_full_percentages_agg_as_metadata.csv"
data = pd.read_csv(data_file_path, delimiter="\t")

special_data_file_path = "../../data/graphs/metadata/V4SubprefixHijackScenario_scenario_none_type_others_policies_none_rov_0_hash_False_probe_True_tunnel_neustar_relay_False_attackRelay_1_attacker_16000_trials_[0.99]_percentages_agg_as_metadata.csv"
special_data = pd.read_csv(special_data_file_path, delimiter="\t")

# %% Preview Data Columns
data.columns.to_list()

# %%#############################
# Preprocessing
################################

# Analysis of 99% point
num_adopting_ases_at_99_perc = dm.num_stubs_of_multihomed_ases * 0.99
num_non_adopting_ases_at_99_perc = (
    dm.num_stubs_of_multihomed_ases - num_adopting_ases_at_99_perc
)

special_data["all_reasons"] = (
    special_data.empty_rib.fillna(0)
    + special_data.no_providers.fillna(0)
    + special_data.no_legit_origin_prefix.fillna(0)
)


# %%-----------------------------
# Classes, Enums, and  Funcs
# -------------------------------


class ProviderSetting(Enum):
    NO_ADOPTING_PROVIDERS = "noad"
    AT_LEAST_1_ADOPTING_PROVIDER = "al1ad"
    ALL_ADOPTING_PROVIDERS = "allad"


class TopologySection(Enum):
    EDGE = "edge"
    ETC = "etc"
    INPUT_CLIQUE = "clique"
    ALL = "all"


class Outcomes(Enum):
    HIJACKED = "hijacked"
    VICTIM_SUCCESS = "successful"
    DISCONNECTED = "disconnected"


def get_column_name(
    adopting, provider_setting, using_adopting_provider, topology_section, outcome
):
    adoption_setting = "ad" if adopting else "nonad"
    using_adopting_provider_setting = "using" if using_adopting_provider else "notusing"
    return "_".join(
        [
            adoption_setting,
            provider_setting.value,
            using_adopting_provider_setting,
            topology_section.value,
            outcome.value,
        ]
    )


def convert_data_as_fraction(
    adopting=True,
    provider_setting=ProviderSetting.ALL_ADOPTING_PROVIDERS,
    topology_section=TopologySection.EDGE,
    outcome=Outcomes.VICTIM_SUCCESS,
):
    total = None
    feature_total = None
    for outcome_i in (
        Outcomes.VICTIM_SUCCESS,
        Outcomes.HIJACKED,
        Outcomes.DISCONNECTED,
    ):
        for using_adopting_provider_setting in (True, False):
            feature = get_column_name(
                adopting,
                provider_setting,
                using_adopting_provider_setting,
                topology_section,
                outcome_i,
            )
            # Total for the selected outcome
            if outcome_i == outcome:
                if feature_total is not None:
                    feature_total = feature_total + data[feature].fillna(0)
                else:
                    feature_total = data[feature].fillna(0)
            # Total for all outcomes
            if total is not None:
                total = total + data[feature].fillna(0)
            else:
                total = data[feature].fillna(0)

    # Create new feature name
    # Remove the using_adopting_provider_setting attribute of name
    result_feature_new_name = (
        get_column_name(
            adopting,
            provider_setting,
            using_adopting_provider_setting,
            topology_section,
            outcome,
        )
        .replace("_notusing", "")
        .replace("_using", "")
    )

    # Compute new feature fraction
    data[result_feature_new_name] = feature_total / total
    # data[result_feature_new_name] = feature_total
    result_feature_new_name_total = result_feature_new_name.replace(
        "_" + outcome.value, ""
    )
    data[result_feature_new_name_total] = total

    # Return name of new feature
    return result_feature_new_name


# %%-----------------------------
# Aggregate
# -------------------------------

# Select Columns
# ---------------------------
# Adopting ASes
# EDGE
# VICTIM SUCCESS
# ---------------------------

# outcome_setting = Outcomes.DISCONNECTED
# adoption_setting = True

for adoption_setting in (True, False):
    for outcome_setting in (
        Outcomes.HIJACKED,
        Outcomes.VICTIM_SUCCESS,
        Outcomes.DISCONNECTED,
    ):
        # All Adopting Providers
        adopting_all_providers = convert_data_as_fraction(
            adopting=adoption_setting,
            provider_setting=ProviderSetting.ALL_ADOPTING_PROVIDERS,
            topology_section=TopologySection.EDGE,
            outcome=outcome_setting,
        )

        # At least 1 adopting provider
        adopting_al1ad_providers = convert_data_as_fraction(
            adopting=adoption_setting,
            provider_setting=ProviderSetting.AT_LEAST_1_ADOPTING_PROVIDER,
            topology_section=TopologySection.EDGE,
            outcome=outcome_setting,
        )

        # No adopting providers
        adopting_no_providers = convert_data_as_fraction(
            adopting=adoption_setting,
            provider_setting=ProviderSetting.NO_ADOPTING_PROVIDERS,
            topology_section=TopologySection.EDGE,
            outcome=outcome_setting,
        )

        # #%% Perform the aggregation
        data_agg = (
            data.groupby(["percentage", "propagation_round", "adoption_setting"])
            .agg(
                {
                    adopting_all_providers: ["mean", dm.calc_90_per_conf],
                    adopting_al1ad_providers: ["mean", dm.calc_90_per_conf],
                    adopting_no_providers: ["mean", dm.calc_90_per_conf],
                }
            )
            .reset_index()
        )
        # data_agg = data.groupby(['percentage', 'propagation_round', 'adoption_setting']).agg({adopting_all_providers: ['mean',],
        #                                                                                       adopting_al1ad_providers: ['mean', ],
        #                                                                                       adopting_no_providers: ['mean', ]}).reset_index()
        data_agg.columns = list(map("".join, data_agg.columns.values))

        # #%%
        # melted_data_agg = pd.melt(data_agg,
        #                           id_vars=['percentage', 'propagation_round', 'adoption_setting'])

        # #%%#############################
        # # Plotting
        #################################

        # adoption_setting_melted_data_agg = melted_data_agg[melted_data_agg.adoption_setting == 'ROV++ V1 Lite Simple Overlayed']
        # px.line(adoption_setting_melted_data_agg, x='percentage', y='value', color='variable', markers='.')

        # #%%
        # px.box(data[data.percentage == 0.99], y='nonad_noad_edge')

        # #%% Matplotlib Line Plot
        _fig, _ax = plt.subplots()

        # plt.xticks([int(x*100) for x in lines[0]._get_x()])
        plt.xticks([0, 20, 40, 60, 80, 100])

        # Making an axis instance
        _ax = _fig.add_axes([0, 0, 1, 1])

        # Make Plot
        colors = ("C0", "C1", "C2")
        markers = (".", "x", "+")
        line_stype = ("solid", "dotted", "dashed")
        labels = (
            "All Providers Adopting",
            "At Least 1 Adopting Provider",
            "No Adopting Providers",
        )
        for i, feature in enumerate(
            (adopting_all_providers, adopting_al1ad_providers, adopting_no_providers)
        ):
            df = data_agg[
                data_agg.adoption_setting == dm.policy_name_map[bgp_immunity_policy]
            ]
            _ax.errorbar(
                df.percentage * 100,
                df[feature + "mean"] * 100,
                yerr=df[feature + "calc_90_per_conf"] * 100,
                marker=markers[i],
                linestyle=line_stype[i],
                color=colors[i],
                label=labels[i],
            )

        # Set Y and X axis Labels
        # As well as output filename component
        # Y axis Label
        metric = None
        if outcome_setting == Outcomes.HIJACKED:
            _ax.set_ylabel(f"Attacker Success")
            metric = "attacker_success"
        elif outcome_setting == Outcomes.VICTIM_SUCCESS:
            _ax.set_ylabel(f"Successful Connections")
            metric = "successful_connections"
        elif outcome_setting == Outcomes.DISCONNECTED:
            _ax.set_ylabel(f"Disconnections")
            metric = "disconnections"
        else:
            raise f"Unknown outcome_setting: {outcome_setting}"

        # X Axis label
        _ax.set_xlabel("Percent adoption")
        _ax.legend(loc="best")

        _fig.set_dpi(150)

        _fig.set_size_inches(5, 4, forward=True)
        ylim = 100
        plt.ylim(0, ylim)
        plt.xlim(0, 100)
        plt.gca().yaxis.grid()
        # plt.tight_layout()
        plt.rcParams.update({"font.size": 12, "lines.markersize": 8})

        adopting_str = "non_adopting_" if not adoption_setting else ""
        policy_dir = "immunity" if bgp_immunity_policy == "rovppo" else "pheme"

        plt.savefig(
            f"./immunity_paper_plots/{policy_dir}/subprefix/rov_{rov_setting}/{adopting_str}incentive_analysis_{relay}_{metric}.pdf",
            bbox_inches="tight",
        )
