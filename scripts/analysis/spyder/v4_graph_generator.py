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
two_attacker_color = 'C1'
five_attacker_color = 'C2'

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
    'ROV adopting': {'color': rov_color, 'marker': default_marker, 'linestyle': default_style},
    'BGPIm adopting': {'color': bgp_immunity_color, 'marker': triangle_marker, 'linestyle': solid_style},
    
      # ARTEMIS
    'ARTEMIS Verisign - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
    'ARTEMIS Verisign - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
    'ARTEMIS Verisign - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
    'ARTEMIS Akamai - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'ARTEMIS Akamai - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'ARTEMIS Akamai - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
    'ARTEMIS Cloudflare - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
    'ARTEMIS Cloudflare - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
    'ARTEMIS Cloudflare - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
    'ARTEMIS Incapsula - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
    'ARTEMIS Incapsula - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
    'ARTEMIS Incapsula - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
    'ARTEMIS Neustar - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
    'ARTEMIS Neustar - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
    'ARTEMIS Neustar - 5 Attackers': {'color': five_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
    # BGPImMS
    'BGPImMS adopting': {'color': k2_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=2 adopting': {'color': k2_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=5 adopting': {'color': k5_color, 'marker': star_marker, 'linestyle': dashed_style},
    'BGPImMS k=10 adopting': {'color': k10_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'BGPIm Verisign - adopting': {'color': verisign_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - adopting': {'color': verisign_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=2 adopting': {'color': verisign_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=5 adopting': {'color': verisign_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=10 adopting': {'color': verisign_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'BGPIm Akamai - adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=2 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=5 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=10 adopting': {'color': akamai_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'BGPIm Cloudflare - adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=2 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=5 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=10 adopting': {'color': cloudflare_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'BGPIm Incapsula - adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=2 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=5 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=10 adopting': {'color': incapsula_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'BGPIm Neustar - adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=2 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=5 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=10 adopting': {'color': neustar_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'BGPIm Conglomerate - adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=2 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=5 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=10 adopting': {'color': neustar_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'BGPIm Ally 5 - adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 5 - adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=2 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=5 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=10 adopting': {'color': five_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 10 - adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=2 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=5 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=10 adopting': {'color': ten_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'BGPIm Ally 20 - adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=2 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=5 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=10 adopting': {'color': twenty_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 40 - adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=2 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=5 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=10 adopting': {'color': Ally_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 50 - adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=2 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=5 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=10 adopting': {'color': fifty_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 100 - adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=2 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=5 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=10 adopting': {'color': hundred_color, 'marker': horizontal_line, 'linestyle': dotted_style},   
    
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}

compare_policies_linemap = {
    # BGPImMS
    'BGPImMS adopting': {'color': bgpim_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=2 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=5 adopting': {'color': bgpim_ms_color, 'marker': star_marker, 'linestyle': dashed_style},
    'BGPImMS k=10 adopting': {'color': bgpim_ms_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'BGPIm Verisign - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'BGPIm Akamai - adopting': {'color': bgpim_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=2 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=5 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=10 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'BGPIm Cloudflare - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'BGPIm Incapsula - adopting': {'color': bgpim_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=2 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=5 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=10 adopting': {'color': bgpim_ms_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'BGPIm Neustar - adopting': {'color': bgpim_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=2 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=5 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=10 adopting': {'color': bgpim_ms_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'BGPIm Conglomerate - adopting': {'color': bgpim_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=2 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=5 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=10 adopting': {'color': bgpim_ms_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'BGPIm Ally 5 - adopting': {'color': bgpim_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 5 - adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=2 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=5 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=10 adopting': {'color': bgpim_ms_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 10 - adopting': {'color': bgpim_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=2 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=5 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=10 adopting': {'color': bgpim_ms_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'BGPIm Ally 20 - adopting': {'color': bgpim_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=2 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=5 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=10 adopting': {'color': bgpim_ms_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 40 - adopting': {'color': bgpim_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=2 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=5 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=10 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 50 - adopting': {'color': bgpim_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=2 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=5 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=10 adopting': {'color': bgpim_ms_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 100 - adopting': {'color': bgpim_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=2 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=5 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=10 adopting': {'color': bgpim_ms_color, 'marker': horizontal_line, 'linestyle': dotted_style},   
    
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}


compare_policies_by_attack_relay_linemap = {
    # BGPImMS
    'BGPImMS adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=2 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS k=5 adopting': {'color': not_attacked_color, 'marker': star_marker, 'linestyle': dashed_style},
    'BGPImMS k=10 adopting': {'color': not_attacked_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'BGPIm Verisign - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'BGPIm Akamai - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=2 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=5 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Akamai - k=10 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'BGPIm Cloudflare - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Cloudflare - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'BGPIm Incapsula - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=2 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=5 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Incapsula - k=10 adopting': {'color': not_attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'BGPIm Neustar - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=2 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=5 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Neustar - k=10 adopting': {'color': not_attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'BGPIm Conglomerate - adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=2 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=5 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Conglomerate - k=10 adopting': {'color': not_attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'BGPIm Ally 5 - adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 5 - adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=2 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=5 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=10 adopting': {'color': not_attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 10 - adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=2 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=5 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=10 adopting': {'color': not_attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'BGPIm Ally 20 - adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=2 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=5 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=10 adopting': {'color': not_attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 40 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=2 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=5 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=10 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 50 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=2 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=5 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=10 adopting': {'color': not_attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Ally 100 - adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=2 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=5 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=10 adopting': {'color': not_attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    
    # ---------------------------------------------------------------------------------------------------------------------------
    
    'BGPImMS Attacked adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked k=2 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked k=5 adopting': {'color': attacked_color, 'marker': star_marker, 'linestyle': dashed_style},
    'BGPImMS Attacked k=10 adopting': {'color': attacked_color, 'marker': pentagon_marker, 'linestyle': dashdot_style},
    
    'BGPIm Attacked Verisign - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Attacked Verisign - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Attacked Verisign - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Attacked Verisign - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Attacked Verisign - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': verisign_style},
    
    'BGPIm Attacked Akamai - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Attacked Akamai - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Attacked Akamai - k=2 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Attacked Akamai - k=5 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    'BGPImMS Attacked Akamai - k=10 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': akamai_style},
    
    'BGPIm Attacked Cloudflare - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Cloudflare - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Cloudflare - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Cloudflare - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Cloudflare - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': cloudflare_style},
    
    'BGPIm Attacked Incapsula - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Attacked Incapsula - adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Attacked Incapsula - k=2 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Attacked Incapsula - k=5 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    'BGPImMS Attacked Incapsula - k=10 adopting': {'color': attacked_color, 'marker': plus_marker, 'linestyle': incapsula_style},
    
    'BGPIm Attacked Neustar - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Attacked Neustar - adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Attacked Neustar - k=2 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Attacked Neustar - k=5 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    'BGPImMS Attacked Neustar - k=10 adopting': {'color': attacked_color, 'marker': default_marker, 'linestyle': neustar_style},
    
    'BGPIm Attacked Conglomerate - adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Conglomerate - adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Conglomerate - k=2 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Conglomerate - k=5 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},
    'BGPImMS Attacked Conglomerate - k=10 adopting': {'color': attacked_color, 'marker': circle_marker, 'linestyle': cloudflare_style},

    'BGPIm Attacked Ally 5 - adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},    
    'BGPImMS Attacked Ally 5 - adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 5 - k=2 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 5 - k=5 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 5 - k=10 adopting': {'color': attacked_color, 'marker': square_marker, 'linestyle': dotted_style},
    
    'BGPIm Attacked Ally 10 - adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 10 - adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 10 - k=2 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 10 - k=5 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 10 - k=10 adopting': {'color': attacked_color, 'marker': thin_diamond, 'linestyle': dotted_style},
    
    'BGPIm Attacked Ally 20 - adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 20 - adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 20 - k=2 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 20 - k=5 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 20 - k=10 adopting': {'color': attacked_color, 'marker': triangle_marker, 'linestyle': dotted_style},
    
    'BGPIm Attacked Ally 40 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 40 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 40 - k=2 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 40 - k=5 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 40 - k=10 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Attacked Ally 50 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 50 - adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 50 - k=2 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 50 - k=5 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 50 - k=10 adopting': {'color': attacked_color, 'marker': vertical_line, 'linestyle': dotted_style},   
    
    'BGPIm Attacked Ally 100 - adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 100 - adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 100 - k=2 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 100 - k=5 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    'BGPImMS Attacked Ally 100 - k=10 adopting': {'color': attacked_color, 'marker': horizontal_line, 'linestyle': dotted_style},
    
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
}



linemap_2 = {
    # ROV
    'ROV adopting': {'color': rov_color, 'marker': default_marker, 'linestyle': default_style},
    # ROV++
    'ROV++ V1 Lite adopting': {'color': rovpp_v1_lite_color, 'marker': x_marker, 'linestyle': loosely_dotted_style},
    # BGPImMS
    'BGPImMS Verisign - k=2 adopting': {'color': 'C0', 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=5 adopting': {'color': 'C1', 'marker': plus_marker, 'linestyle': verisign_style},
    'BGPImMS Verisign - k=10 adopting': {'color': 'C2', 'marker': plus_marker, 'linestyle': verisign_style},
    
    'BGPImMS Ally 5 - k=2 adopting': {'color': 'C0', 'marker': pentagon_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=5 adopting': {'color': 'C1', 'marker': pentagon_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=10 adopting': {'color': 'C2', 'marker': pentagon_marker, 'linestyle': dotted_style},

}

compare_relays_linemap = {
    # BGPImMS
    'BGPIm Verisign - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Verisign - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Verisign - k=2 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Verisign - k=5 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Verisign - k=10 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': 'dashed'},

    'BGPIm Akamai - adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},    
    'BGPImMS Akamai - adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Akamai - k=2 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Akamai - k=5 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Akamai - k=10 adopting': {'color': 'C1', 'marker': default_marker, 'linestyle': 'dashed'},
    
    'BGPIm Cloudflare - adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Cloudflare - adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Cloudflare - k=2 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Cloudflare - k=5 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Cloudflare - k=10 adopting': {'color': 'C2', 'marker': default_marker, 'linestyle': 'dashed'},

    'BGPIm Incapsula - adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},    
    'BGPImMS Incapsula - adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Incapsula - k=2 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Incapsula - k=5 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Incapsula - k=10 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': 'dashed'},

    'BGPIm Neustar - adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},    
    'BGPImMS Neustar - adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Neustar - k=2 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Neustar - k=5 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Neustar - k=10 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': 'dashed'},
    
    'BGPIm Conglomerate - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},    
    'BGPImMS Conglomerate - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Conglomerate - k=2 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Conglomerate - k=5 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},
    'BGPImMS Conglomerate - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': 'dashed'},

    'BGPIm Ally 5 - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 5 - adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 5 - k=2 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=5 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 5 - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 10 - adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=2 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=5 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 10 - k=10 adopting': {'color': 'C6', 'marker': default_marker, 'linestyle': dotted_style},

    'BGPIm Ally 20 - adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 20 - adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 20 - k=2 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=5 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 20 - k=10 adopting': {'color': 'C7', 'marker': default_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 40 - adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 40 - adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 40 - k=2 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=5 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 40 - k=10 adopting': {'color': 'C8', 'marker': default_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 50 - adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 50 - adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 50 - k=2 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=5 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 50 - k=10 adopting': {'color': 'C9', 'marker': default_marker, 'linestyle': dotted_style},
    
    'BGPIm Ally 100 - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 100 - adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},    
    'BGPImMS Ally 100 - k=2 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=5 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
    'BGPImMS Ally 100 - k=10 adopting': {'color': 'C0', 'marker': default_marker, 'linestyle': dotted_style},
}



def create_compare_cdn_linemap(cdn):
    return {
            
        f'BGPImMS {cdn} - k=2 adopting': {'color': 'C0', 'marker': plus_marker, 'linestyle': verisign_style},
        f'BGPImMS {cdn} - k=5 adopting': {'color': 'C1', 'marker': plus_marker, 'linestyle': verisign_style},
        f'BGPImMS {cdn} - k=10 adopting': {'color': 'C2', 'marker': plus_marker, 'linestyle': verisign_style},
        
        f'BGPImMS {cdn} Attacked - k=2 adopting': {'color': 'C3', 'marker': default_marker, 'linestyle': solid_style},
        f'BGPImMS {cdn} Attacked - k=5 adopting': {'color': 'C4', 'marker': default_marker, 'linestyle': solid_style},
        f'BGPImMS {cdn} Attacked - k=10 adopting': {'color': 'C5', 'marker': default_marker, 'linestyle': solid_style},
    }


# For ARTEMIS Plots
# linemap = {
#     'BGP': {'color': baseline_color, 'marker': baseline_marker, 'linestyle': default_style},
#     'BGP+100% ROV': {'color': baseline_color, 'marker': '', 'linestyle': default_style},
#     'ARTEMIS Verisign - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
#     'ARTEMIS Verisign - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': verisign_style},
#     'ARTEMIS Verisign - 5 Attackers': {'color': 'C0', 'marker': default_marker, 'linestyle': verisign_style},
#     'ARTEMIS Akamai - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
#     'ARTEMIS Akamai - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': akamai_style},
#     'ARTEMIS Akamai - 5 Attackers': {'color': 'C1', 'marker': default_marker, 'linestyle': akamai_style},
#     'ARTEMIS Cloudflare - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
#     'ARTEMIS Cloudflare - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': cloudflare_style},
#     'ARTEMIS Cloudflare - 5 Attackers': {'color': 'C2', 'marker': default_marker, 'linestyle': cloudflare_style},
#     'ARTEMIS Incapsula - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
#     'ARTEMIS Incapsula - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': incapsula_style},
#     'ARTEMIS Incapsula - 5 Attackers': {'color': 'C3', 'marker': default_marker, 'linestyle': incapsula_style},
#     'ARTEMIS Neustar - 1 Attackers': {'color': one_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
#     'ARTEMIS Neustar - 2 Attackers': {'color': two_attacker_color, 'marker': default_marker, 'linestyle': neustar_style},
#     'ARTEMIS Neustar - 5 Attackers': {'color': 'C4', 'marker': default_marker, 'linestyle': neustar_style},
# }

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
                 alpha=1):
    fig, ax = plt.subplots()

    # plt.xlim(0, 1.3)
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
                    label="" if (line.label in used_labels) else line.label,
                    color=linemap[line.label]['color'],
                    marker=linemap[line.label]["marker"],
                    path_effects=[path_effects.SimpleLineShadow(offset=(0, -0.5)), path_effects.Normal()],
                    alpha=alpha)

        used_labels.add(line.label)

    assert outcome_text, "Missing outcome_text"
    ax.set_ylabel(f"{outcome_text}")
    ax.set_xlabel("Percent adoption")

    # Might throw warnings later?
    # redundant?
    # legend = plt.legend()
    # print(legend.get_texts()) #[0].set_text('make it short')
    plt.tight_layout()
    plt.rcParams.update({"font.size": 12, "lines.markersize": 8})
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
