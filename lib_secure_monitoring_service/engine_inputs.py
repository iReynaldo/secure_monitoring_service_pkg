from lib_rovpp import ROVPPSubprefixHijack

from .TrustedServer import TrustedServer


class V4SubprefixHijack(ROVPPSubprefixHijack):
    def post_propagation_hook(self, engine, data_point, *args, **kwargs):
        """Runs after a round of propagation"""

        # For each AS
        for as_obj in engine:
            # Clear the AS, but not the relationship info or server info
            as_obj.__init__(reset_base=False, reset_trusted_server=False)
            # Set the trusted server flag to True
            if hasattr(as_obj, "trusted_server"):
                as_obj.trusted_server.make_recs = True
