from lib_bgp_simulator import Outcomes, Relationships

from lib_rovpp import ROVPPSubprefixHijack

from secure_monitoring_service_pkg.simulation_framework.sim_logger import sim_logger as logger


class V4SubprefixHijack(ROVPPSubprefixHijack):

    # TODO: Move this into the new Scenario Class
    def determine_outcome(self, as_obj, ann):
        """This assumes that the as_obj is the last in the path"""

        if self.attacker_asn == as_obj.asn:
            return Outcomes.ATTACKER_SUCCESS, as_obj.asn
        elif self.victim_asn == as_obj.asn:
            return Outcomes.VICTIM_SUCCESS, as_obj.asn
        # End of traceback. Didn't reach atk/vic so it's disconnected
        # Note that there is no good way to end, which is why we have
        # The traceback_end just in case
        # Since paths could be lies, and for things like blackholes
        # The recv relationship must not be the origin
        elif (ann is None or
              len(ann.as_path) == 1
              or ann.recv_relationship == Relationships.ORIGIN
              or ann.traceback_end):

            return Outcomes.DISCONNECTED, as_obj.asn
        # Keep going
        else:
            return None, as_obj.asn

    def post_propagation_hook(self, engine, data_point, *args, **kwargs):
        """Runs after a round of propagation"""
        logger.info("Entered Post propagation hook")
        # For each AS
        # trust_server_reference = None
        # for as_obj in engine:
        #     # # Clear the AS, but not the relationship info or server info
        #     # as_obj.__init__(reset_base=False, reset_trusted_server=False)
        #     # Set the trusted server flag to True
        #     if hasattr(as_obj, "trusted_server"):
        #     #     # as_obj.trusted_server._make_recs = True
        #     #     print("Local RIB: ", as_obj._local_rib)
        #     #     for rib_entry in as_obj._local_rib:
        #     #         if rib_entry == "1.2.0.0/16":
        #     #             ann = as_obj._local_rib["1.2.0.0/16"]\
        #         trust_server_reference =  as_obj.trusted_server
        # if trust_server_reference:
        #     trust_server_reference.create_recs()
        #     path_list = trust_server_reference.reports_to_path_list("1.2.3.0/24")
        #     from secure_monitoring_service_pkg.mvdp import get_avoid_list
        #     print("Path List: ", trust_server_reference.reports_to_path_list("1.2.3.0/24"))
        #     print("Avoid List: ", trust_server_reference._recommendations)
