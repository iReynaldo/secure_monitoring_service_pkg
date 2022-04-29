from lib_rovpp import ROVPPSubprefixHijack
from lib_secure_monitoring_service.sim_logger import sim_logger as logger


class V4SubprefixHijack(ROVPPSubprefixHijack):

    def post_propagation_hook(self, engine, data_point, *args, **kwargs):
        """Runs after a round of propagation"""
        logger.info("Entered Post propagation hook")
        # # For each AS
        # trust_server_reference = None
        # for as_obj in engine:
        #     # Clear the AS, but not the relationship info or server info
        #     as_obj.__init__(reset_base=False, reset_trusted_server=False)
        #     # Set the trusted server flag to True
        #     if hasattr(as_obj, "trusted_server"):
        #         as_obj.trusted_server._make_recs = True
        #         trust_server_reference =  as_obj.trusted_server
        # # if trust_server_reference:
        # #     trust_server_reference.create_recs()