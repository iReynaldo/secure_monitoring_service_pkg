import random
import math

from typing import Tuple, Optional, Type, Set, Dict, List, Union
from ipaddress import ip_network

from caida_collector_pkg import AS

from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Timestamps
from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import SpecialPercentAdoptions
from bgp_simulator_pkg import RealROVSimpleAS

from .cdn import CDN
from .peer import Peer
from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger

################################
# Constants
################################

CDN_RELAY_SETTING = "cdn"
PEER_RELAY_SETTING = "peer"
CUSTOM_RELAY_SETTING = "custom"
NO_RELAY_SETTING = "no_relay"

RELAY_PREFIX = "7.7.7.0/24"


################################
# Functions
################################

def select_fraction_from_set(iterable_obj, fraction):
    """

    :param iterable_obj:
    :param fraction: a float between 0 and 1 (all-inclusive)
    :return:
    """
    # Calculate number of items to select, where at least 1 is chosen.
    fraction_to_select = max(round(len(iterable_obj) * fraction), 1)
    # Recommended from python error message to use sorted for set and dict objects
    return random.sample(sorted(iterable_obj), fraction_to_select)


################################
# Main Scenario Class
################################

class V4Scenario(Scenario):

    def __init__(self, *args, relay_asns=None, attack_relays=False, fraction_of_peer_ases_to_attack=0.5,
                 assume_relays_are_reachable=False, tunnel_customers_traffic=False,
                 probe_data_plane=False, special_static_as_class=None, **kwargs):
        super(V4Scenario, self).__init__(*args, **kwargs)
        self.has_rovsms_ases = False
        self.trusted_server_ref = None
        self.avoid_lists = None  # Used for verifying avoid list
        self.name = "V4Scenario"
        self.relay_prefixes: Dict[int, str] = dict()
        self.relay_asns = relay_asns
        self.tunnel_customers_traffic = tunnel_customers_traffic
        self.assume_relays_are_reachable = assume_relays_are_reachable
        self.attack_relays = attack_relays
        self.fraction_of_peer_ases_to_attack = fraction_of_peer_ases_to_attack
        self.probe_data_plane = probe_data_plane
        self.special_static_as_class = special_static_as_class if special_static_as_class else RealROVSimpleAS
        self.relay_setting = None
        self.relay_name = None
        if relay_asns:
            if self._is_using_cdn(relay_asns):
                self.relay_setting = CDN_RELAY_SETTING
                self.relay_name = CDN().reverse_mapping[self.relay_asns]
            elif self._is_using_peer(relay_asns):
                self.relay_setting = PEER_RELAY_SETTING
                self.relay_name = Peer().reverse_mapping[self.relay_asns]
            else:
                self.relay_setting = CUSTOM_RELAY_SETTING
                self.relay_name = CUSTOM_RELAY_SETTING
        else:
            self.relay_setting = NO_RELAY_SETTING

    def _is_using_cdn(self, relay_asns):
        if relay_asns == CDN().akamai or relay_asns == CDN().cloudflare or \
                relay_asns == CDN().verisign or relay_asns == CDN().incapsula or \
                relay_asns == CDN().neustar or relay_asns == CDN().conglomerate:
            return True
        else:
            return False

    def _is_using_peer(self, relay_asns):
        if relay_asns == Peer().five or relay_asns == Peer().ten or \
                relay_asns == Peer().twenty or relay_asns == Peer().forty or \
                relay_asns == Peer().fifty or relay_asns == Peer().hundred:
            return True
        else:
            return False

    @property
    def _default_adopters(self) -> Set[int]:
        """By default, victim always adopts"""
        if self.relay_asns:
            return self.victim_asns | self.relay_asns
        else:
            return self.victim_asns

    def apply_blackholes_from_avoid_list(self, engine):
        logger.debug(f"Inside apply_blackholes_from_avoid_list")
        # Create a flag to check if avoid_list has been created
        avoid_list_created_flag = False
        # Iterate over all adopting ASNs
        # TODO: Does non_default_as_cls_dict also contain ROV ASes when
        #  doing mixed deployment?
        for asn in self.non_default_as_cls_dict:
            # Get reference to AS Object
            as_obj = engine.as_dict[asn]
            # TODO: Remove this check if ROV ASes are not in
            #  non_default_as_cls_dict when doing Mixed Deployment.
            if hasattr(as_obj, "trusted_server"):
                # Create avoid list if it hasn't been created yet
                if not avoid_list_created_flag:
                    self.trusted_server_ref = as_obj.trusted_server
                    # Let Trusted Server know the current scenario information
                    self.trusted_server_ref.scenario_name = self.name
                    # Compute the avoid list
                    as_obj.trusted_server.create_recs()
                    self.avoid_lists = self.trusted_server_ref._recommendations
                    avoid_list_created_flag = True
                    self.has_rovsms_ases = True

                as_obj._force_add_blackholes_from_avoid_list(self.ordered_prefix_subprefix_dict)

    def _get_adopting_asns_dict(
            self,
            engine: SimulationEngine,
            percent_adopt: Union[float, SpecialPercentAdoptions]
    ) -> Dict[int, Type[AS]]:
        """
        This is a copy of the one in the super class with a single variable change
        to allow different ASes to be set instead of just ROV for these special mixed
        adoption setting
        """

        asn_cls_dict = dict()
        for subcategory in self.adoption_subcategory_attrs:
            ases = getattr(engine, subcategory)
            real_rov_ases = set()
            # If we are including ROV nodes
            # Don't always run this to save on time
            if self.min_rov_confidence <= 1:
                for as_ in ases:
                    if as_.rov_confidence >= self.min_rov_confidence:
                        asn_cls_dict[as_.asn] = self.special_static_as_class  # Change made here
                        real_rov_ases.add(as_)
            # Remove ASes that are already pre-set
            # Ex: Attacker and victim
            # Ex: ROV Nodes (in certain situations)
            possible_adopters = ases.difference(self._preset_asns)
            possible_adopters = possible_adopters.difference(real_rov_ases)

            # Get how many ASes should be adopting

            # Round for the start and end of the graph
            # (if 0 ASes would be adopting, have 1 as adopt)
            # (If all ASes would be adopting, have all -1 adopt)
            # This was a feature request, but it's not supported
            if percent_adopt == SpecialPercentAdoptions.ONLY_ONE:
                k = 1
            elif percent_adopt == SpecialPercentAdoptions.ALL_BUT_ONE:
                k = len(possible_adopters) - 1
            else:
                assert isinstance(percent_adopt, float), "Make mypy happy"
                k = math.ceil(len(possible_adopters) * percent_adopt)

            # https://stackoverflow.com/a/15837796/8903959
            possible_adopters = tuple(possible_adopters)
            try:
                for as_ in random.sample(possible_adopters, k):
                    asn_cls_dict[as_.asn] = self.AdoptASCls
            except ValueError:
                raise ValueError(
                    f"{k} can't be sampled from {len(possible_adopters)}")
            for asn in self._default_adopters:
                asn_cls_dict[asn] = self.AdoptASCls
        return asn_cls_dict

    def _get_ordered_prefix_subprefix_dict(self):
        """Saves a dict of prefix to subprefixes

        mypy was having a lot of trouble with this section
        thus the type ignores
        """

        prefixes = set([])
        all_announcements_including_not_sent = set()
        all_announcements_including_not_sent.update(self.announcements)
        all_announcements_including_not_sent.update(self.get_attacker_announcements())
        for ann in all_announcements_including_not_sent:
            prefixes.add(ann.prefix)
        # Do this here for speed
        prefixes: List[Union[IPv4Network, IPv6Network]] = [  # type: ignore
            ip_network(x) for x in prefixes]
        # Sort prefixes with most specific prefix first
        # Note that this must be sorted for the traceback to get the
        # most specific prefix first
        prefixes = list(sorted(prefixes,
                               key=lambda x: x.num_addresses))  # type: ignore

        prefix_subprefix_dict = {x: [] for x in prefixes}  # type: ignore
        for outer_prefix, subprefix_list in prefix_subprefix_dict.items():
            for prefix in prefixes:
                if (prefix.subnet_of(outer_prefix)  # type: ignore
                        and prefix != outer_prefix):
                    subprefix_list.append(str(prefix))
        # Get rid of ip_network
        self.ordered_prefix_subprefix_dict: Dict[str, List[str]] = {
            str(k): v for k, v in prefix_subprefix_dict.items()}

    def pre_aggregation_hook(self, **kwargs):
        """
        kwargs should contain the following
        {
            "engine": SimulationEngine,
            "percent_adopt": float,
            "trial": int,
            "scenario": Scenario,
            "propagation_round": int
        }
        """
        # Add blackholes from avoid list
        engine = kwargs["engine"]
        self.apply_blackholes_from_avoid_list(engine)
        # Add blackhole information to trusted server
        if self.trusted_server_ref:
            for attacker_ann in self.get_attacker_announcements_for_origin():
                self.trusted_server_ref.gather_blackhole_information(attacker_ann.prefix, engine)

    def post_propagation_hook(self, *args, **kwargs):
        # TODO: Verify if this will continue to work
        # Emtpy the trusted server
        if self.trusted_server_ref:
            self.trusted_server_ref.reset()
            # Note the trusted_server_ref is set inside apply_blackholes_from_avoid_list
            self.trusted_server_ref = None
        # Delete saved avoid list
        self.avoid_lists = None

    def determine_as_outcome(self,
                             as_obj: AS,
                             ann: Optional[Announcement]
                             ) -> Tuple[Type[Outcomes], Type[int]]:
        """Determines the outcome at an AS

        ann is most_specific_ann is the most specific prefix announcement
        that exists at that AS
        """

        if as_obj.asn in self.attacker_asns:
            return Outcomes.ATTACKER_SUCCESS, as_obj.asn
        elif as_obj.asn in self.victim_asns:
            return Outcomes.VICTIM_SUCCESS, as_obj.asn
        # End of traceback
        elif (ann is None
              or len(ann.as_path) == 1
              or ann.recv_relationship == Relationships.ORIGIN
              or ann.traceback_end):
            return Outcomes.DISCONNECTED, as_obj.asn
        else:
            return Outcomes.UNDETERMINED, as_obj.asn

    def get_attacker_announcements(self):
        attacker_announcements = set()
        for ann in self.announcements:
            for attacker_asn in self.attacker_asns:
                if attacker_asn in ann.as_path:
                    attacker_announcements.add(ann)
        return attacker_announcements

    def get_attacker_announcements_for_origin(self):
        """
        These are the attacker announcements that target the origin
        :return:
        """
        anns = set()
        # Get origin prefix
        origin_prefix = next(iter(self.get_victim_announcements())).prefix
        origin_prefix_network = ip_network(origin_prefix)
        # Identify the attacker announcement that attacks the origin prefix
        for attacker_ann in self.get_attacker_announcements():
            attacker_prefix_network = ip_network(attacker_ann.prefix)
            if attacker_prefix_network.subnet_of(origin_prefix_network):
                anns.add(attacker_ann)
        return anns

    def get_victim_announcements(self):
        victim_announcements = set()
        for ann in self.announcements:
            for victim_asn in self.victim_asns:
                if victim_asn in ann.as_path:
                    victim_announcements.add(ann)
        return victim_announcements

    def create_attacker_relay_announcement(self, prefix, seed_asn, roa_origin):
        return self.AnnCls(prefix=prefix,
                           as_path=(seed_asn,),
                           timestamp=Timestamps.ATTACKER.value,
                           seed_asn=seed_asn,
                           roa_valid_length=True,
                           roa_origin=roa_origin,
                           recv_relationship=Relationships.ORIGIN)

    def generate_relay_announcements(self, providers_dict=None):
        anns = list()
        roa_origin: int = next(iter(self.victim_asns))
        # Setup Relay Announcements
        if self.relay_asns:
            for i, relay_asn in enumerate(self.relay_asns):
                relay_prefix = RELAY_PREFIX if self.relay_setting == CDN_RELAY_SETTING else f"{i + 1}.{i + 1}.{i + 1}.0/24"
                self.relay_prefixes[relay_asn] = relay_prefix
                anns.append(self.AnnCls(prefix=relay_prefix,
                                        as_path=(relay_asn,),
                                        timestamp=Timestamps.VICTIM.value,
                                        seed_asn=relay_asn,
                                        roa_valid_length=True,
                                        roa_origin=relay_asn,
                                        recv_relationship=Relationships.ORIGIN))
                if providers_dict:
                    providers_dict[relay_prefix] = relay_asn  # This is not really needed for autoimmune attack
            # Add Attacker announcements for relays
            if self.attack_relays:
                if self.relay_setting == CDN_RELAY_SETTING:
                    for attacker_asn in self.attacker_asns:
                        anns.append(self.create_attacker_relay_announcement(RELAY_PREFIX, attacker_asn, roa_origin))
                else:
                    for attacker_asn in self.attacker_asns:
                        for relay_prefix in select_fraction_from_set(self.relay_prefixes.values(), self.fraction_of_peer_ases_to_attack):
                            anns.append(self.create_attacker_relay_announcement(relay_prefix, attacker_asn, roa_origin))
        return anns

    def get_victim_asn(self, **kwargs):
        # Note: assumption there is 1 victim
        return next(iter(self.victim_asns))

    def _get_possible_attacker_asns(
            self,
            engine: SimulationEngine,
            percent_adoption: Union[float, SpecialPercentAdoptions],
            prev_scenario: Optional["Scenario"]
    ) -> Set[int]:
        """
        Returns possible attacker ASNs, defaulted from stubs_and_mh
        This is a direct copy of the parent class with the addition of removing
        the relay ASNs.
        """

        err = "Make mypy happy"
        assert all(isinstance(x, int) for x in engine.stub_or_mh_asns), err
        assert isinstance(engine.stub_or_mh_asns, set), err
        if self.relay_asns:
            return engine.stub_or_mh_asns - self.relay_asns
        else:
            return engine.stub_or_mh_asns

    def _get_possible_victim_asns(
            self,
            engine: SimulationEngine,
            percent_adoption: Union[float, SpecialPercentAdoptions],
            prev_scenario: Optional["Scenario"]
    ) -> Set[int]:
        """
        Returns possible victim ASNs, defaulted from stubs_and_mh
        This is a direct copy of the parent class with the addition of removing
        the relay ASNs.
        """

        err = "Make mypy happy"
        assert all(isinstance(x, int) for x in engine.stub_or_mh_asns), err
        assert isinstance(engine.stub_or_mh_asns, set), err
        if self.relay_asns:
            return engine.stub_or_mh_asns - self.relay_asns
        else:
            return engine.stub_or_mh_asns
