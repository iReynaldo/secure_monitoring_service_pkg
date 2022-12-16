from typing import Tuple, Optional, Type

from caida_collector_pkg import AS

from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Relationships
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Announcement

from secure_monitoring_service_pkg.simulation_framework.sim_logger \
    import sim_logger as logger


class V4Scenario(Scenario):

    def __init__(self, *args, **kwargs):
        super(V4Scenario, self).__init__(*args, **kwargs)
        self.has_rovsms_ases = False
        self.trusted_server_ref = None
        self.avoid_lists = None  # Used for verifying avoid list
        self.name = "V4Scenario"

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