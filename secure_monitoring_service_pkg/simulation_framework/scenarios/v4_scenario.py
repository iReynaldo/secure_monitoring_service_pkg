from typing import Tuple, Optional, Type, Set, Dict, List
from ipaddress import ip_network

from caida_collector_pkg import AS

from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Announcement
from bgp_simulator_pkg import Timestamps


from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger


################################
# Main Scenario Class
################################

class V4Scenario(Scenario):

    def __init__(self, *args, relay_asns=None, attack_relays=False,
                 assume_relays_are_reachable=False, tunnel_customer_traffic=False, **kwargs):
        super(V4Scenario, self).__init__(*args, **kwargs)
        self.has_rovsms_ases = False
        self.trusted_server_ref = None
        self.avoid_lists = None  # Used for verifying avoid list
        self.name = "V4Scenario"
        self.relay_asns = relay_asns
        self.tunnel_customer_traffic = tunnel_customer_traffic
        self.assume_relays_are_reachable = assume_relays_are_reachable
        self.attack_relays = attack_relays
        self.relay_prefixes = dict()

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
        self.apply_blackholes_from_avoid_list(kwargs["engine"])

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

    def get_victim_announcements(self):
        victim_announcements = set()
        for ann in self.announcements:
            for victim_asn in self.victim_asns:
                if victim_asn in ann.as_path:
                    victim_announcements.add(ann)
        return victim_announcements

    def generate_relay_announcements(self):
        anns = list()
        roa_origin: int = next(iter(self.victim_asns))
        # Setup Relay Announcements
        if self.relay_asns:
            for i, relay_asn in enumerate(self.relay_asns):
                relay_prefix = f"{i + 1}.{i + 1}.{i + 1}.0/24"
                self.relay_prefixes[relay_asn] = relay_prefix
                anns.append(self.AnnCls(prefix=relay_prefix,
                                        as_path=(relay_asn,),
                                        timestamp=2,
                                        seed_asn=relay_asn,
                                        roa_valid_length=True,
                                        roa_origin=relay_asn,
                                        recv_relationship=Relationships.ORIGIN))
                # Add Attacker announcements for relays
                if self.attack_relays:
                    for attacker_asn in self.attacker_asns:
                        anns.append(self.AnnCls(prefix=relay_prefix,
                                                as_path=(attacker_asn,),
                                                timestamp=Timestamps.ATTACKER.value,
                                                seed_asn=attacker_asn,
                                                roa_valid_length=False,
                                                roa_origin=roa_origin,
                                                recv_relationship=Relationships.ORIGIN))
        return anns

    def get_victim_asn(self, **kwargs):
        # Note: assumption there is 1 victim
        return next(iter(self.victim_asns))
