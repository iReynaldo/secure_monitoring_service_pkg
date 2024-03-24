import sys
import os
from textwrap import wrap
from math import sqrt
from enum import Enum
import json
from copy import deepcopy
from statistics import mean, stdev
from collections import defaultdict

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
# import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio


# Colors
baseline_color = 'C7'  # grey

one_attacker_color = 'C0'
two_attacker_color = 'C2'
five_attacker_color = 'C1'

bgpim_color = 'C0'
bgpim_ms_color = 'C1'

not_attacked_color ='C2'
attacked_color = 'C3'

rov_color = 'C7'
bgp_immunity_color = 'C6'
rovpp_v1_lite_color = 'C3'
k2_color = 'C0'
k5_color = 'C1'
k10_color = 'C2'

akamai_color = 'C0'
cloudflare_color  = 'C4'
verisign_color = 'C4'
incapsula_color  = 'C4'
neustar_color  =  'C4'
rov_color  =  'C5'
Ally_color = 'C8'
five_color  =  Ally_color
ten_color  =  Ally_color
twenty_color  =  Ally_color
forty_color = Ally_color
fifty_color = Ally_color
hundred_color = Ally_color


# Line Styles
solid_style = 'solid'
dotted_style = 'dotted'
dashed_style = 'dashed'
dashdot_style = 'dashdot'
loosely_dotted_style = (0, (1, 10))  # Loosely dotted


default_style = 'dashed'
akamai_style = 'dashed'
cloudflare_style = 'dashed'
verisign_style = 'dashed'
incapsula_style = 'dashed'
neustar_style = (0, (1, 10))  # Loosely dotted

# Markers
default_marker = '.'
plus_marker = 'P'
pentagon_marker = 'p'
star_marker = '*'
triangle_marker = '^'
square_marker = 's'
x_marker = 'x'
thin_diamond = 'd'
x_filled_marker = 'X'
vertical_line = '|'
horizontal_line = '_'
circle_marker = 'o'


linemap = {
    'BGP': {'color': baseline_color, 'marker': default_marker, 'linestyle': default_style},
    'ROV adopting': {'label': 'ROV', 'color': rov_color, 'marker': circle_marker, 'linestyle': default_style, 'markerfacecolor': False},
    'Overlay adopting': {'color': bgp_immunity_color, 'marker': triangle_marker, 'linestyle': solid_style},
    
    # Minverva Origin Only (Receiver)
    'Minerva (Receiver Origin Only) Verisign - adopting': {'label': 'Receiver-based origin-only CDN (VE)', 'color': 'C8', 'marker': x_filled_marker, 'linestyle': dotted_style},
    'Minerva (Receiver Origin Only) Neustar - adopting': {'label': 'Receiver-based origin-only CDN (NE)', 'color': two_attacker_color, 'marker': star_marker, 'linestyle': dotted_style},
    'Minerva (Receiver Origin Only) Cloudflare - adopting': {'label': 'Origin-only, current ROV', 'color': 'C6', 'marker': thin_diamond, 'linestyle': solid_style},
    'Minerva (Receiver Origin Only) Cloudflare - adopting No ROV': {'label': 'Origin-only, no ROV', 'color': 'C6', 'marker': thin_diamond, 'linestyle': dotted_style, 'markerfacecolor': False},
    'Minerva (Receiver CDN Only) Verisign - adopting': {'color': five_attacker_color, 'marker': star_marker, 'linestyle': verisign_style},
    'Minerva (Receiver CDN Only) Neustar - adopting': {'color': five_attacker_color, 'marker': thin_diamond, 'linestyle': neustar_style},
    'Minerva (Receiver CDN Only) Cloudflare - adopting': {'color': five_attacker_color, 'marker': square_marker, 'linestyle': cloudflare_style},

    # Minerva (Receiver)default_marker
    'Minerva (Receiver) Verisign - adopting': {'label': 'Receiver-based CDN (VE)', 'color': one_attacker_color, 'marker': x_filled_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Verisign - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
    'Minerva (Receiver) Verisign - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
    'Minerva (Receiver) Akamai - adopting': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Receiver) Akamai - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Receiver) Akamai - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Receiver) Cloudflare - adopting': {'label': 'w/  CDN (CF), current ROV', 'color': 'orange', 'marker': plus_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Cloudflare - adopting No ROV': {'label': 'w/  CDN (CF), no ROV', 'color': 'orange', 'marker': plus_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    'Minerva (Receiver) Cloudflare - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
    'Minerva (Receiver) Cloudflare - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
    'Minerva (Receiver) Cloudflare - 5 Attackers No ROV': {'label': 'CDN (CF), no ROV', 'color': five_attacker_color, 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Receiver) Incapsula - adopting': {'label': 'Receiver-based CDN (IC)', 'color': one_attacker_color, 'marker': default_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Incapsula - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
    'Minerva (Receiver) Incapsula - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
    'Minerva (Receiver) Neustar - adopting': {'label': 'Receiver-based CDN (NE)', 'color': one_attacker_color, 'marker': thin_diamond, 'linestyle': solid_style},
    'Minerva (Receiver) Neustar - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Receiver) Neustar - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
    # Minerva (Sender)
    'Minerva (Sender) adopting': {'color': k2_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=2 adopting': {'color': k2_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=5 adopting': {'color': k5_color, 'marker': star_marker, 'linestyle': dashed_style},
    'Minerva (Sender) k=10 adopting': {'color': k10_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'Overlay Verisign - adopting': {'color': verisign_color, 'marker': x_filled_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - adopting': {'label': 'M-Adopter, CDN (VE)', 'color': verisign_color, 'marker': x_filled_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=2 adopting': {'color': verisign_color, 'marker': x_filled_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=5 adopting': {'color': verisign_color, 'marker': x_filled_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=10 adopting': {'color': verisign_color, 'marker': x_filled_marker, 'linestyle': verisign_style},
    
    'Overlay Akamai - adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=2 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=5 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=10 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'Overlay Cloudflare - adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - adopting': {'label': 'M-Adopter, CDN (CF)', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=2 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=5 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=10 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'Overlay Incapsula - adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=2 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=5 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=10 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'Overlay Neustar - adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=2 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=5 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=10 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'Overlay Conglomerate - adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=2 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=5 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=10 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'Overlay Ally 5 - adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 5 - adopting': {'label': 'M-Adopter, Ally (k=5)', 'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=2 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=5 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=10 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 10 - adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=2 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=5 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=10 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'Overlay Ally 20 - adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - adopting': {'label': 'M-Adopter, Ally (k=20)', 'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=2 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=5 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=10 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 40 - adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=2 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=5 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=10 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 50 - adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=2 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=5 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=10 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 100 - adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=2 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=5 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=10 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},   
    
    # ROV++
    'ROV++ V1 Lite adopting': {'label': 'ROV++', 'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}

receiver_base_compare_rov = {                    
    'Minerva (Receiver) Cloudflare - adopting (1 Attackers)': {'label': '1 attacker, w/ CDN (CF), current ROV', 'color': 'C1', 'marker': circle_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Cloudflare - adopting (20 Attackers)': {'label': '20 attackers, w/ CDN (CF), current ROV', 'color': 'C2', 'marker': thin_diamond, 'linestyle': solid_style},
    'Minerva (Receiver) Cloudflare - adopting (1 Attackers) No ROV': {'label': '1 attacker, w/ CDN (CF), no ROV', 'color': 'C1', 'marker': circle_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    'Minerva (Receiver) Cloudflare - adopting (20 Attackers) No ROV': {'label': '20 attackers, w/ CDN (CF), no ROV', 'color': 'C2', 'marker': thin_diamond, 'linestyle': dotted_style, 'markerfacecolor': False},
    
    'Minerva (Receiver Origin Only) Cloudflare - adopting (1 Attackers)': {'label': '1 attacker, origin-only, current ROV', 'color': 'C1', 'marker': circle_marker, 'linestyle': solid_style},
    'Minerva (Receiver Origin Only) Cloudflare - adopting (20 Attackers)': {'label': '20 attackers, origin-only, current ROV', 'color': 'C2', 'marker': thin_diamond, 'linestyle': solid_style},
    'Minerva (Receiver Origin Only) Cloudflare - adopting (1 Attackers) No ROV': {'label': '1 attacker, origin-only, no ROV', 'color': 'C1', 'marker': circle_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    'Minerva (Receiver Origin Only) Cloudflare - adopting (20 Attackers) No ROV': {'label': '20 attackers, origin-only, no ROV', 'color': 'C2', 'marker': thin_diamond, 'linestyle': dotted_style, 'markerfacecolor': False},
}


compare_policies_linemap = {
    # Minerva (Sender)
    'Minerva (Sender) adopting': {'color': bgpim_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=2 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=5 adopting': {'color': bgpim_ms_color, 'marker': star_marker, 'linestyle': dashed_style},
    'Minerva (Sender) k=10 adopting': {'color': bgpim_ms_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'Overlay Verisign - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - adopting': {'label': 'CDN (VE)','color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'Overlay Akamai - adopting': {'color': bgpim_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=2 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=5 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=10 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'Overlay Cloudflare - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - adopting': {'label': 'CDN (CF)','color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Cloudflare - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'Overlay Incapsula - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'Overlay Neustar - adopting': {'color': bgpim_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=2 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=5 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=10 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'Overlay Conglomerate - adopting': {'color': bgpim_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=2 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=5 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=10 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'Overlay Ally 5 - adopting': {'color': bgpim_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 5 - adopting': {'label': 'Ally (k=5)', 'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=2 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=5 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=10 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 10 - adopting': {'color': bgpim_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=2 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=5 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=10 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'Overlay Ally 20 - adopting': {'color': bgpim_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - adopting': {'label': 'Ally (k=20)', 'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=2 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=5 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=10 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 40 - adopting': {'color': bgpim_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=2 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=5 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=10 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 50 - adopting': {'color': bgpim_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=2 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=5 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=10 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 100 - adopting': {'color': bgpim_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=2 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=5 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=10 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},   
    
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}

# num_attackers_linemap = {
#     'ROV, 1 attacker': {'label': 'ROV, 1 attacker','color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},
#     'ROV, 5 attackers': {'label': 'ROV, 5 attackers', 'color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},

#     'ROV++, 1 attacker': {'label': 'ROV++, 1 attacker', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},
#     'ROV++, 5 attackers': {'label': 'ROV++, 5 attackers', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},

#     'ROV CDN (CF), 1 attacker': {'label': 'ROV CDN (CF), 1 attacker', 'color': 'blue', 'marker': plus_marker, 'linestyle': 'solid'},
#     'ROV CDN (CF), 5 attackers': {'label': 'ROV CDN (CF), 5 attackers', 'color': 'blue', 'marker': plus_marker, 'linestyle': 'solid'},
    
#     'ROV++ CDN (CF), 1 attacker': {'label': 'ROV++ CDN (CF), 1 attacker', 'color': 'green', 'marker': thin_diamond, 'linestyle': 'solid'},
#     'ROV++ CDN (CF), 5 attackers': {'label': 'ROV++ CDN (CF), 5 attackers', 'color': 'green', 'marker': thin_diamond, 'linestyle': 'solid'},
# }

num_attackers_linemap = {
    'ROV, 1 attacker': {'label': 'ROV','color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},
    'ROV, 5 attackers': {'label': 'ROV', 'color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},

    'ROV++, 1 attacker': {'label': 'ROV++', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},
    'ROV++, 5 attackers': {'label': 'ROV++', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},

    'ROV CDN (CF), 1 attacker': {'label': 'ROV, CDN (CF)', 'color': 'blue', 'marker': plus_marker, 'linestyle': 'solid'},
    'ROV CDN (CF), 5 attackers': {'label': 'ROV, CDN (CF)', 'color': 'blue', 'marker': plus_marker, 'linestyle': 'solid'},
    
    'ROV++ CDN (CF), 1 attacker': {'label': 'ROV++, CDN (CF)', 'color': 'green', 'marker': thin_diamond, 'linestyle': 'solid'},
    'ROV++ CDN (CF), 5 attackers': {'label': 'ROV++, CDN (CF)', 'color': 'green', 'marker': thin_diamond, 'linestyle': 'solid'},
}

# main_num_attackers_linemap = {
#     'ROV, 1 attacker': {'label': 'ROV, 1 attacker','color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},
#     'ROV, 5 attackers': {'label': 'ROV, 5 attackers', 'color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},

#     'ROV++, 1 attacker': {'label': 'ROV++, 1 attacker', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},
#     'ROV++, 5 attackers': {'label': 'ROV++, 5 attackers', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},

#     'CDN (CF), 1 attacker': {'label': 'CDN (CF), 1 attacker', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': 'solid'},
#     'Sender-based CDN (CF), 5 attackers': {'label': 'CDN (CF), 5 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': dotted_style},
#     'Sender-based CDN (CF), 10 attackers': {'label': 'CDN (CF), 10 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': 'dashed'},
#     'Sender-based CDN (CF), 20 attackers': {'label': 'CDN (CF), 20 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
#     'Sender-based Ally (k=5), 1 attacker': {'label': 'Ally (k=5), 1 attacker', 'color': five_color, 'marker': square_marker, 'linestyle': 'solid'},
#     'Sender-based Ally (k=5), 5 attackers': {'label': 'Ally (k=5), 5 attackers', 'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
#     'Sender-based Ally (k=5), 10 attackers': {'label': 'Ally (k=5), 10 attackers', 'color': five_color, 'marker': square_marker, 'linestyle': 'dashed'},
#     'Sender-based Ally (k=5), 20 attackers': {'label': 'Ally (k=5), 20 attackers', 'color': five_color, 'marker': square_marker, 'linestyle': loosely_dotted_style},
    
#     'Receiver-based CDN (CF), 1 attacker': {'label': 'Receiver-based CDN (CF), 1 attacker', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': 'solid'},
#     'Receiver-based CDN (CF), 5 attackers': {'label': 'Receiver-based CDN (CF), 5 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
#     'Receiver-based CDN (CF), 10 attackers': {'label': 'Receiver-based CDN (CF), 10 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': 'dashed'},
#     'Receiver-based CDN (CF), 20 attackers': {'label': 'Receiver-based CDN (CF), 20 attackers', 'color': cloudflare_color, 'marker': plus_marker, 'linestyle': loosely_dotted_style, 'markerfacecolor': False},
    
#     'Receiver-based CDN (VE), 1 attacker': {'label': 'Receiver-based CDN (VE), 1 attacker', 'color': five_color, 'marker': x_filled_marker, 'linestyle': 'solid'},
#     'Receiver-based CDN (VE), 5 attackers': {'label': 'Receiver-based CDN (VE), 5 attackers', 'color': five_color, 'marker': x_filled_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
#     'Receiver-based CDN (VE), 10 attackers': {'label': 'Receiver-based CDN (VE), 10 attackers', 'color': five_color, 'marker': x_filled_marker, 'linestyle': 'dashed'},
#     'Receiver-based CDN (VE), 20 attackers': {'label': 'Receiver-based CDN (VE), 20 attackers', 'color': five_color, 'marker': x_filled_marker, 'linestyle': loosely_dotted_style, 'markerfacecolor': False},
    
    
#     # 'label': 'Ally (k=5)'
# }

ATTACKER_1_COLOR = 'C0'
ATTACKER_5_COLOR = 'C3'
ATTACKER_10_COLOR = 'C2'
ATTACKER_20_COLOR = 'C1'

main_num_attackers_linemap = {
    'ROV, 1 attacker': {'label': 'ROV, 1 attacker','color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},
    'ROV, 5 attackers': {'label': 'ROV, 5 attackers', 'color': rov_color, 'marker': circle_marker, 'linestyle': 'solid', 'markerfacecolor': False},

    'ROV++, 1 attacker': {'label': 'ROV++, 1 attacker', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},
    'ROV++, 5 attackers': {'label': 'ROV++, 5 attackers', 'color': 'red', 'marker': x_marker, 'linestyle': 'solid'},

    'Sender-based CDN (CF), 1 attacker': {'label': 'CDN (CF), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (CF), 5 attackers': {'label': 'CDN (CF), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (CF), 10 attackers': {'label': 'CDN (CF), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (CF), 20 attackers': {'label': 'CDN (CF), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Sender-based CDN (VE), 1 attacker': {'label': 'CDN (VE), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (VE), 5 attackers': {'label': 'CDN (VE), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (VE), 10 attackers': {'label': 'CDN (VE), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (VE), 20 attackers': {'label': 'CDN (VE), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Sender-based CDN (NE), 1 attacker': {'label': 'CDN (NE), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (NE), 5 attackers': {'label': 'CDN (NE), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (NE), 10 attackers': {'label': 'CDN (NE), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (NE), 20 attackers': {'label': 'CDN (NE), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Sender-based CDN (AK), 1 attacker': {'label': 'CDN (AK), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (AK), 5 attackers': {'label': 'CDN (AK), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (AK), 10 attackers': {'label': 'CDN (AK), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (AK), 20 attackers': {'label': 'CDN (AK), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Sender-based CDN (IN), 1 attacker': {'label': 'CDN (IN), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (IN), 5 attackers': {'label': 'CDN (IN), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (IN), 10 attackers': {'label': 'CDN (IN), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (IN), 20 attackers': {'label': 'CDN (IN), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Sender-based Ally (k=5), 1 attacker': {'label': 'Ally (k=5), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': square_marker, 'linestyle': 'solid'},
    'Sender-based Ally (k=5), 5 attackers': {'label': 'Ally (k=5), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': square_marker, 'linestyle': dotted_style},
    'Sender-based Ally (k=5), 10 attackers': {'label': 'Ally (k=5), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': square_marker, 'linestyle': 'dashed'},
    'Sender-based Ally (k=5), 20 attackers': {'label': 'Ally (k=5), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': square_marker, 'linestyle': dotted_style},
    
    # 'Receiver-based CDN (CF), 1 attacker': {'label': 'Receiver-based CDN (CF), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    # 'Receiver-based CDN (CF), 5 attackers': {'label': 'Receiver-based CDN (CF), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    # 'Receiver-based CDN (CF), 10 attackers': {'label': 'Receiver-based CDN (CF), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    # 'Receiver-based CDN (CF), 20 attackers': {'label': 'Receiver-based CDN (CF), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    
    # 'Receiver-based CDN (VE), 1 attacker': {'label': 'Receiver-based CDN (VE), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': x_filled_marker, 'linestyle': 'solid'},
    # 'Receiver-based CDN (VE), 5 attackers': {'label': 'Receiver-based CDN (VE), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': x_filled_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    # 'Receiver-based CDN (VE), 10 attackers': {'label': 'Receiver-based CDN (VE), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': x_filled_marker, 'linestyle': 'dashed'},
    # 'Receiver-based CDN (VE), 20 attackers': {'label': 'Receiver-based CDN (VE), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': x_filled_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    
    'Receiver-based CDN (CF), 1 attacker': {'label': 'Receiver-based CDN (CF), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (CF), 5 attackers': {'label': 'Receiver-based CDN (CF), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (CF), 10 attackers': {'label': 'Receiver-based CDN (CF), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (CF), 20 attackers': {'label': 'Receiver-based CDN (CF), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Receiver-based CDN (VE), 1 attacker': {'label': 'Receiver-based CDN (VE), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': x_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (VE), 5 attackers': {'label': 'Receiver-based CDN (VE), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': x_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (VE), 10 attackers': {'label': 'Receiver-based CDN (VE), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': x_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (VE), 20 attackers': {'label': 'Receiver-based CDN (VE), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': x_marker, 'linestyle': dotted_style},
    
    'Receiver-based CDN (NE), 1 attacker': {'label': 'Receiver-based CDN (NE), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (NE), 5 attackers': {'label': 'Receiver-based CDN (NE), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (NE), 10 attackers': {'label': 'Receiver-based CDN (NE), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (NE), 20 attackers': {'label': 'Receiver-based CDN (NE), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Receiver-based CDN (AK), 1 attacker': {'label': 'Receiver-based CDN (AK), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (AK), 5 attackers': {'label': 'Receiver-based CDN (AK), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (AK), 10 attackers': {'label': 'Receiver-based CDN (AK), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (AK), 20 attackers': {'label': 'Receiver-based CDN (AK), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Receiver-based CDN (IN), 1 attacker': {'label': 'Receiver-based CDN (IN), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (IN), 5 attackers': {'label': 'Receiver-based CDN (IN), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (IN), 10 attackers': {'label': 'Receiver-based CDN (IN), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (IN), 20 attackers': {'label': 'Receiver-based CDN (IN), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    
    # 'label': 'Ally (k=5)'
}

main_num_attackers_ally_linemap = {
    'Sender-based Ally (k=5), 1 attacker': {'label': 'Ally (k=5), 1 attacker', 'color': ATTACKER_1_COLOR, 'marker': circle_marker, 'linestyle': 'solid'},
    'Sender-based Ally (k=5), 5 attackers': {'label': 'Ally (k=5), 5 attackers', 'color': ATTACKER_5_COLOR, 'marker': square_marker, 'linestyle': loosely_dotted_style},
    'Sender-based Ally (k=5), 10 attackers': {'label': 'Ally (k=5), 10 attackers', 'color': ATTACKER_10_COLOR, 'marker': x_filled_marker, 'linestyle': 'dashed'},
    'Sender-based Ally (k=5), 20 attackers': {'label': 'Ally (k=5), 20 attackers', 'color': ATTACKER_20_COLOR, 'marker': triangle_marker, 'linestyle': dotted_style},
}



CLOUDFLARE_COLOR= 'C0'
VERISIGN_COLOR = 'C1'
NEUSTAR_COLOR = 'C2'
AKAMAI_COLOR = 'C3'
INCAPSULA_COLOR = 'C4'

compare_cdns_linemap = {
    'Sender-based CDN (CF), 1 attacker': {'label': 'CDN (CF)', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (CF), 5 attackers': {'label': 'CDN (CF)', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (CF), 10 attackers': {'label': 'CDN (CF)', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (CF), 20 attackers': {'label': 'CDN (CF)', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Sender-based CDN (VE), 1 attacker': {'label': 'CDN (VE)', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (VE), 5 attackers': {'label': 'CDN (VE)', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (VE), 10 attackers': {'label': 'CDN (VE)', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (VE), 20 attackers': {'label': 'CDN (VE)', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Sender-based CDN (NE), 1 attacker': {'label': 'CDN (NE)', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (NE), 5 attackers': {'label': 'CDN (NE)', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (NE), 10 attackers': {'label': 'CDN (NE)', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (NE), 20 attackers': {'label': 'CDN (NE)', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Sender-based CDN (AK), 1 attacker': {'label': 'CDN (AK)', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (AK), 5 attackers': {'label': 'CDN (AK)', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (AK), 10 attackers': {'label': 'CDN (AK)', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (AK), 20 attackers': {'label': 'CDN (AK)', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Sender-based CDN (IN), 1 attacker': {'label': 'CDN (IN)', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Sender-based CDN (IN), 5 attackers': {'label': 'CDN (IN)', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Sender-based CDN (IN), 10 attackers': {'label': 'CDN (IN)', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Sender-based CDN (IN), 20 attackers': {'label': 'CDN (IN)', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Sender-based Ally (k=5), 1 attacker': {'label': 'Ally (k=5)', 'color': ATTACKER_1_COLOR, 'marker': square_marker, 'linestyle': 'solid'},
    'Sender-based Ally (k=5), 5 attackers': {'label': 'Ally (k=5)', 'color': ATTACKER_5_COLOR, 'marker': square_marker, 'linestyle': dotted_style},
    'Sender-based Ally (k=5), 10 attackers': {'label': 'Ally (k=5)', 'color': ATTACKER_10_COLOR, 'marker': square_marker, 'linestyle': 'dashed'},
    'Sender-based Ally (k=5), 20 attackers': {'label': 'Ally (k=5)', 'color': ATTACKER_20_COLOR, 'marker': square_marker, 'linestyle': loosely_dotted_style},
    
    # 'Receiver-based CDN (CF), 1 attacker': {'label': 'Receiver-based CDN (CF), 1', 'color': ATTACKER_1_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    # 'Receiver-based CDN (CF), 5 attackers': {'label': 'Receiver-based CDN (CF), 5', 'color': ATTACKER_5_COLOR, 'marker': plus_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    # 'Receiver-based CDN (CF), 10 attackers': {'label': 'Receiver-based CDN (CF), 10', 'color': ATTACKER_10_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    # 'Receiver-based CDN (CF), 20 attackers': {'label': 'Receiver-based CDN (CF), 20', 'color': ATTACKER_20_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style, 'markerfacecolor': False},
    
    # 'Receiver-based CDN (VE), 1 attacker': {'label': 'Receiver-based CDN (VE), 1', 'color': ATTACKER_1_COLOR, 'marker': x_filled_marker, 'linestyle': 'solid'},
    # 'Receiver-based CDN (VE), 5 attackers': {'label': 'Receiver-based CDN (VE), 5', 'color': ATTACKER_5_COLOR, 'marker': x_filled_marker, 'linestyle': dotted_style, 'markerfacecolor': False},
    # 'Receiver-based CDN (VE), 10 attackers': {'label': 'Receiver-based CDN (VE), 10', 'color': ATTACKER_10_COLOR, 'marker': x_filled_marker, 'linestyle': 'dashed'},
    # 'Receiver-based CDN (VE), 20 attackers': {'label': 'Receiver-based CDN (VE), 20', 'color': ATTACKER_20_COLOR, 'marker': x_filled_marker, 'linestyle': loosely_dotted_style, 'markerfacecolor': False},
    
    'Receiver-based CDN (CF), 1 attacker': {'label': 'Receiver-based CDN (CF), 1', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (CF), 5 attackers': {'label': 'Receiver-based CDN (CF), 5', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (CF), 10 attackers': {'label': 'Receiver-based CDN (CF), 10', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (CF), 20 attackers': {'label': 'Receiver-based CDN (CF), 20', 'color': CLOUDFLARE_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Receiver-based CDN (VE), 1 attacker': {'label': 'Receiver-based CDN (VE), 1', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (VE), 5 attackers': {'label': 'Receiver-based CDN (VE), 5', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (VE), 10 attackers': {'label': 'Receiver-based CDN (VE), 10', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (VE), 20 attackers': {'label': 'Receiver-based CDN (VE), 20', 'color': VERISIGN_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    
    'Receiver-based CDN (NE), 1 attacker': {'label': 'Receiver-based CDN (NE), 1', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (NE), 5 attackers': {'label': 'Receiver-based CDN (NE), 5', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (NE), 10 attackers': {'label': 'Receiver-based CDN (NE), 10', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (NE), 20 attackers': {'label': 'Receiver-based CDN (NE), 20', 'color': NEUSTAR_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Receiver-based CDN (AK), 1 attacker': {'label': 'Receiver-based CDN (AK), 1', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (AK), 5 attackers': {'label': 'Receiver-based CDN (AK), 5', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (AK), 10 attackers': {'label': 'Receiver-based CDN (AK), 10', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (AK), 20 attackers': {'label': 'Receiver-based CDN (AK), 20', 'color': AKAMAI_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    'Receiver-based CDN (IN), 1 attacker': {'label': 'Receiver-based CDN (IN), 1', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': 'solid'},
    'Receiver-based CDN (IN), 5 attackers': {'label': 'Receiver-based CDN (IN),  5', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': dotted_style},
    'Receiver-based CDN (IN), 10 attackers': {'label': 'Receiver-based CDN (IN), 10', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': 'dashed'},
    'Receiver-based CDN (IN), 20 attackers': {'label': 'Receiver-based CDN (IN), 20', 'color': INCAPSULA_COLOR, 'marker': plus_marker, 'linestyle': loosely_dotted_style},
    
    # 'label': 'Ally (k=5)'
}

compare_policies_by_attack_relay_linemap = {
    
    # Minerva (Receiver)
    'Minerva (Receiver) adopting': {'color': not_attacked_color, 'marker': star_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Verisign - adopting': {'label': 'Receiver-based CDN (VE)', 'color': not_attacked_color, 'marker': star_marker, 'linestyle': solid_style},
    'Minerva (Receiver) Neustar - adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': solid_style},
    'Minerva (Receiver) Cloudflare - adopting': {'label': 'Receiver-based CDN (CF)', 'color': not_attacked_color, 'marker': square_marker, 'linestyle': solid_style},

    # Minerva (Sender)
    'Minerva (Sender) adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=2 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) k=5 adopting': {'color': not_attacked_color, 'marker': star_marker, 'linestyle': dashed_style},
    'Minerva (Sender) k=10 adopting': {'color': not_attacked_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'Overlay Verisign - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'Overlay Akamai - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=2 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=5 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Akamai - k=10 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'Overlay Cloudflare - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': solid_style},
    'Minerva (Sender) Cloudflare - adopting': {'label': 'CDN (CF), no attack to relay', 'color': not_attacked_color, 'marker': plus_marker, 'linestyle': solid_style},
    'Minerva (Sender) Cloudflare - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': solid_style},
    'Minerva (Sender) Cloudflare - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': solid_style},
    'Minerva (Sender) Cloudflare - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': solid_style},
    
    'Overlay Incapsula - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Incapsula - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'Overlay Neustar - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=2 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=5 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Neustar - k=10 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'Overlay Conglomerate - adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=2 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=5 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Conglomerate - k=10 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'Overlay Ally 5 - adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 5 - adopting': {'label': 'Ally (k=5), no attack to relay', 'color': not_attacked_color, 'marker': square_marker, 'linestyle': solid_style},
    'Minerva (Sender) Ally 5 - k=2 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': solid_style},
    'Minerva (Sender) Ally 5 - k=5 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': solid_style},
    'Minerva (Sender) Ally 5 - k=10 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': solid_style},
    
    'Overlay Ally 10 - adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=2 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=5 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=10 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'Overlay Ally 20 - adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=2 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=5 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=10 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 40 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=2 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=5 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=10 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 50 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=2 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=5 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=10 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Ally 100 - adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=2 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=5 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=10 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    
    # ---------------------------------------------------------------------------------------------------------------------------
    
    # Minerva (Receiver)
    'Minerva (Receiver) Attacked adopting': {'color': attacked_color, 'marker': star_marker, 'linestyle': dotted_style},
    'Minerva (Receiver) Attacked Verisign - adopting': {'label': 'Receiver-based CDN (VE) Attacked', 'color': attacked_color, 'marker': star_marker, 'linestyle': dotted_style},
    'Minerva (Receiver) Attacked Neustar - adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Receiver) Attacked Cloudflare - adopting': {'label': 'Receiver-based CDN (CE) Attacked', 'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    # Minerva (Sender)
    'Minerva (Sender) Attacked adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked k=2 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked k=5 adopting': {'color': attacked_color, 'marker': star_marker, 'linestyle': dashed_style},
    'Minerva (Sender) Attacked k=10 adopting': {'color': attacked_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'Overlay Attacked Verisign - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Attacked Verisign - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Attacked Verisign - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Attacked Verisign - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Attacked Verisign - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'Overlay Attacked Akamai - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Attacked Akamai - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Attacked Akamai - k=2 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Attacked Akamai - k=5 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'Minerva (Sender) Attacked Akamai - k=10 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'Overlay Attacked Cloudflare - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Cloudflare - adopting': {'label': 'CDN (CF), w/ attack to relay', 'color': attacked_color, 'marker': plus_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Cloudflare - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Cloudflare - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Cloudflare - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': dotted_style},
    
    'Overlay Attacked Incapsula - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Attacked Incapsula - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Attacked Incapsula - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Attacked Incapsula - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'Minerva (Sender) Attacked Incapsula - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'Overlay Attacked Neustar - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Attacked Neustar - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Attacked Neustar - k=2 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Attacked Neustar - k=5 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'Minerva (Sender) Attacked Neustar - k=10 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'Overlay Attacked Conglomerate - adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Attacked Conglomerate - adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Attacked Conglomerate - k=2 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Attacked Conglomerate - k=5 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'Minerva (Sender) Attacked Conglomerate - k=10 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'Overlay Attacked Ally 5 - adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Attacked Ally 5 - adopting': {'label': 'Ally (k=5), w/ attack to relay', 'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 5 - k=2 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 5 - k=5 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 5 - k=10 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'Overlay Attacked Ally 10 - adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 10 - adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 10 - k=2 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 10 - k=5 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 10 - k=10 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'Overlay Attacked Ally 20 - adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 20 - adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 20 - k=2 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 20 - k=5 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 20 - k=10 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'Overlay Attacked Ally 40 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 40 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 40 - k=2 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 40 - k=5 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 40 - k=10 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Attacked Ally 50 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 50 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 50 - k=2 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 50 - k=5 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 50 - k=10 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'Overlay Attacked Ally 100 - adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 100 - adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 100 - k=2 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 100 - k=5 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'Minerva (Sender) Attacked Ally 100 - k=10 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}



linemap_2 = {
    # ROV
    'ROV adopting': {'color': rov_color, 'marker': default_marker, 'linestyle': default_style},
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
    # Minerva (Sender)
    'Minerva (Sender) Verisign - k=2 adopting': {'color': 'C0', 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=5 adopting': {'color': 'C1', 'marker': plus_marker, 'linestyle': verisign_style},
    'Minerva (Sender) Verisign - k=10 adopting': {'color': 'C2', 'marker': plus_marker, 'linestyle': verisign_style},
    
    'Minerva (Sender) Ally 5 - k=2 adopting': {'color': 'C0', 'marker': pentagon_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=5 adopting': {'color': 'C1', 'marker': pentagon_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=10 adopting': {'color': 'C2', 'marker': pentagon_marker, 'linestyle': dotted_style},

}

compare_relays_linemap = {
    # Minerva (Sender)
    'Overlay Verisign - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Verisign - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Verisign - k=2 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Verisign - k=5 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Verisign - k=10 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},

    'Overlay Akamai - adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},    
    'Minerva (Sender) Akamai - adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Akamai - k=2 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Akamai - k=5 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Akamai - k=10 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    
    'Overlay Cloudflare - adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Cloudflare - adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Cloudflare - k=2 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Cloudflare - k=5 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Cloudflare - k=10 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},

    'Overlay Incapsula - adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},    
    'Minerva (Sender) Incapsula - adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Incapsula - k=2 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Incapsula - k=5 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Incapsula - k=10 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},

    'Overlay Neustar - adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},    
    'Minerva (Sender) Neustar - adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Neustar - k=2 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Neustar - k=5 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Neustar - k=10 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    
    'Overlay Conglomerate - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},    
    'Minerva (Sender) Conglomerate - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Conglomerate - k=2 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Conglomerate - k=5 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'Minerva (Sender) Conglomerate - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},

    'Overlay Ally 5 - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 5 - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 5 - k=2 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=5 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 5 - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 10 - adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=2 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=5 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 10 - k=10 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},

    'Overlay Ally 20 - adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 20 - adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 20 - k=2 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=5 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 20 - k=10 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 40 - adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 40 - adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 40 - k=2 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=5 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 40 - k=10 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 50 - adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 50 - adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 50 - k=2 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=5 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 50 - k=10 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    
    'Overlay Ally 100 - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 100 - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},    
    'Minerva (Sender) Ally 100 - k=2 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=5 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
    'Minerva (Sender) Ally 100 - k=10 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
}



def create_compare_cdn_linemap(cdn):
    return {
            
        f'Minerva (Sender) {cdn} - k=2 adopting': {'color': 'C0', 'marker': plus_marker, 'linestyle': verisign_style},
        f'Minerva (Sender) {cdn} - k=5 adopting': {'color': 'C1', 'marker': plus_marker, 'linestyle': verisign_style},
        f'Minerva (Sender) {cdn} - k=10 adopting': {'color': 'C2', 'marker': plus_marker, 'linestyle': verisign_style},
        
        f'Minerva (Sender) {cdn} Attacked - k=2 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': solid_style},
        f'Minerva (Sender) {cdn} Attacked - k=5 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': solid_style},
        f'Minerva (Sender) {cdn} Attacked - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': solid_style},
    }


# For Minerva (Receiver) Plots
# linemap = {
#     'BGP': {'color': baseline_color, 'marker': baseline_marker, 'linestyle': default_style},
#     'BGP+100% ROV': {'color': baseline_color, 'marker': '', 'linestyle': default_style},
#     'Minerva (Receiver) Verisign - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
#     'Minerva (Receiver) Verisign - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
#     'Minerva (Receiver) Verisign - 5 Attackers': {'color': 'C0', 'marker': default_marker, 'linestyle': verisign_style},
#     'Minerva (Receiver) Akamai - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
#     'Minerva (Receiver) Akamai - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
#     'Minerva (Receiver) Akamai - 5 Attackers': {'color': 'C1', 'marker': default_marker, 'linestyle': akamai_style},
#     'Minerva (Receiver) Cloudflare - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
#     'Minerva (Receiver) Cloudflare - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
#     'Minerva (Receiver) Cloudflare - 5 Attackers': {'color': 'C2', 'marker': default_marker, 'linestyle': cloudflare_style},
#     'Minerva (Receiver) Incapsula - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
#     'Minerva (Receiver) Incapsula - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
#     'Minerva (Receiver) Incapsula - 5 Attackers': {'color': 'C3', 'marker': default_marker, 'linestyle': incapsula_style},
#     'Minerva (Receiver) Neustar - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
#     'Minerva (Receiver) Neustar - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
#     'Minerva (Receiver) Neustar - 5 Attackers': {'color': 'C4', 'marker': default_marker, 'linestyle': neustar_style},
# }

class Line:
    """Formats raw data for matplotlib graph"""

    def __init__(self, scenario_label, has_connector: bool, percent_adopt_dict, remove_zero_percent_point: bool = True):
        """Stores info aobut a line in a graph"""

        # {percent_adopt: [percentages]}
        self.percent_adopt_dict = percent_adopt_dict
        if remove_zero_percent_point:
            if 0.0 in self.percent_adopt_dict:
                del self.percent_adopt_dict[0.0]
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
            # 2.326  99% confidence interval Z value
            # 1.960  95% confidence interval Z value 
            # 1.645  90% confidence interval Z value
            yerr_num = 1.960 * 2 * stdev(list_of_vals)
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
        def parse(subgraph_name: str, adoption_setting='adopting'):
            result: {ASType: {int, [float]}} = {}
            temp: {ASType: [(int, [float])]} = {}

            for dataset in json_data:
                rates = dataset[subgraph_name][propagation_round][f"{base_policy_name} ({adopting_policy_name} {adoption_setting})"]
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
        
        self.adopting = parse(subgraph_name, 'adopting')
        # self.non_adopting = parse(subgraph_name, 'non-adopting')

def add_value_annotations(x_vals, y_vals, ax):
    for x, y in zip(x_vals, y_vals):
        ax.annotate("{:.1f}".format(y), xy=(x,y))

def generate_plotly(lines: [Line], metric):
    pio.renderers.default = 'browser'
    
    data = defaultdict(list)
    for line in lines:
        data["Percent adoption"].extend(line.x)
        data[metric].extend(line.y)
        data["yerr"].extend(line.yerr)
        data["label"].extend([line.label]*len(line.x))
        
    table = pd.DataFrame(data)

    fig = px.line(table,
                  x="Percent adoption", 
                  y=metric,
                  color="label",
                  error_y="yerr",
                  markers=True)
    fig.show()

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
                 ylim=None,
                 linemap=linemap,
                 show_legend=True,
                 alpha=1,
                 markerfacecolor=None):
    fig, ax = plt.subplots()

    # plt.xlim(0, 1.3)
    if type(ylim) is tuple:
        plt.ylim(ylim[0], ylim[1])
    else:
        ylim = 100 if ylim is None else ylim
        plt.ylim(0, ylim)

    # plt.xticks([int(x*100) for x in lines[0]._get_x()])
    plt.xticks([0, 20, 40, 60, 80, 100])

    used_labels = set()
    
    for line in lines:
        ax.errorbar([x*100 for x in line._get_x()],
                    line.y,
                    yerr=line.yerr,
                    linestyle=linemap[line.label]['linestyle'],# if not line.has_connector else 'None',
                    label="" if (linemap[line.label]['label'] in used_labels) else linemap[line.label]['label'],
                    color=linemap[line.label]['color'],
                    marker=linemap[line.label]["marker"],
                    path_effects=[path_effects.SimpleLineShadow(offset=(0, -0.5)), path_effects.Normal()],
                    alpha=alpha,
                    markerfacecolor=markerfacecolor if linemap[line.label].get('markerfacecolor', True) else 'none',
                    markersize= 8 if linemap[line.label].get('markerfacecolor', True) else 12 )

        used_labels.add(linemap[line.label]['label'])

    assert outcome_text, "Missing outcome_text"
    ax.set_ylabel(f"{outcome_text}")
    ax.set_xlabel("Percent adoption")

    # Might throw warnings later?
    # redundant?
    # legend = plt.legend()
    # print(legend.get_texts()) #[0].set_text('make it short')
    plt.tight_layout()
    plt.rcParams.update({"font.size": 14.5})
    #matplotlib.use('Agg')

    if show_legend:    
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
    # plt.close(fig)
    # plt.cla()
    # plt.clf()
