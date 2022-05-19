from lib_bgp_simulator.simulator.scenario import Scenario
from lib_bgp_simulator.enums import Relationships

from lib_secure_monitoring_service.rov_sms import ROVSMS
from lib_secure_monitoring_service.sim_logger import sim_logger as logger

class V4Scenario(Scenario):


    def apply_blackholes_from_avoid_list(self, subgraphs):
        logger.debug(f"Inside apply_blackholes_from_avoid_list")
        for subg_name, subgraph_asns in subgraphs.items():
            for asn in subgraph_asns:
                as_obj = self.engine.as_dict[asn]
                if hasattr(as_obj, "trusted_server"):
                    new_holes = as_obj._get_ann_to_holes_dict_from_trusted_server(self.engine_input)
                    has_holes_to_process = False
                    if new_holes:
                        for val in new_holes.values():
                            if len(val) != 0:
                                has_holes_to_process = True
                        if has_holes_to_process:
                            logger.debug("New Holes to add: ", new_holes)
                            as_obj._force_add_blackholes(new_holes, Relationships.ORIGIN)


    def run(self, subgraphs, propagation_round: int):
        # Run engine
        self.engine.run(propagation_round=propagation_round,
                        engine_input=self.engine_input)
        # Add blackholes from avoid list
        ROVSMS.trusted_server.create_recs()
        self.apply_blackholes_from_avoid_list(subgraphs)
        # Calculate outcomes
        traceback_outcomes = self._collect_data(subgraphs)
        # Don't count these for diagrams and such
        for uncountable_asn in self.engine_input.uncountable_asns:
            traceback_outcomes.pop(uncountable_asn, None)
        # delete engine from attrs so that garbage collector can come
        # NOTE that if there are multiple propagation rounds, the engine
        # Will still be there
        del self.engine
        # Delete the adopting_asns for the same reason.
        # This does not cause problems for multiple rounds because the AS
        # classes are already set.
        if hasattr(self.engine_input, 'adopting_asns'):
            del self.engine_input.adopting_asns

        return traceback_outcomes