from dataclasses import dataclass
from typing import Any

from bgpy import ScenarioConfig
from bgpy import RealROVSimpleAS

from .cdn import CDN
from .peer import Peer

################################
# Constants
################################

CDN_RELAY_SETTING = "cdn"
PEER_RELAY_SETTING = "peer"
CUSTOM_RELAY_SETTING = "custom"
NO_RELAY_SETTING = "no_relay"


################################
# Main Scenario Class
################################


@dataclass(frozen=True)
class V4ScenarioConfig(ScenarioConfig):
    relay_asns: Any = None
    attack_relays: Any = False
    fraction_of_peer_ases_to_attack: Any = 0.5
    assume_relays_are_reachable: Any = False
    tunnel_customers_traffic: Any = False
    probe_data_plane: Any = False
    special_static_as_class: Any = None
    fightback: Any = False
    # If the autoimmune attack is indirect(True)/direct(False)
    indirect: Any = True

    def __post_init__(self):
        if self.special_static_as_class is None:
            object.__setattr__(self, "special_static_as_class", RealROVSimpleAS)

        relay_setting = None
        relay_name = None
        if self.relay_asns:
            if self._is_using_cdn(self.relay_asns):
                relay_setting = CDN_RELAY_SETTING
                relay_name = CDN().reverse_mapping[self.relay_asns]
            elif self._is_using_peer(self.relay_asns):
                relay_setting = PEER_RELAY_SETTING
                relay_name = Peer().reverse_mapping[self.relay_asns]
            else:
                relay_setting = CUSTOM_RELAY_SETTING
                relay_name = CUSTOM_RELAY_SETTING
        else:
            relay_setting = NO_RELAY_SETTING

        if relay_setting is not None:
            object.__setattr__(self, "relay_setting", relay_setting)
        if relay_name is not None:
            object.__setattr__(self, "relay_name", relay_name)

        super().__post_init__()

    def _is_using_cdn(self, relay_asns):
        if (
            relay_asns == CDN().akamai
            or relay_asns == CDN().cloudflare
            or relay_asns == CDN().verisign
            or relay_asns == CDN().incapsula
            or relay_asns == CDN().neustar
            or relay_asns == CDN().conglomerate
        ):
            return True
        else:
            return False

    def _is_using_peer(self, relay_asns):
        if (
            relay_asns == Peer().five
            or relay_asns == Peer().ten
            or relay_asns == Peer().twenty
            or relay_asns == Peer().forty
            or relay_asns == Peer().fifty
            or relay_asns == Peer().hundred
        ):
            return True
        else:
            return False
