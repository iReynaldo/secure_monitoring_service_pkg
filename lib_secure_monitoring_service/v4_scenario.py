import gc

from lib_bgp_simulator.simulator.scenario import Scenario
from lib_bgp_simulator import enums
from lib_bgp_simulator import BGPAS
from lib_bgp_simulator import Outcomes

from lib_rovpp import ROVPPV1SimpleAS, ROVPPV1LiteSimpleAS
from lib_secure_monitoring_service.rov_sms import ROVSMS
from lib_secure_monitoring_service.sim_logger import sim_logger as logger


class V4Scenario(Scenario):
    trusted_server_ref = None
    avoid_lists = None  # Used for verifying avoid list in pytest system tests
    traceback_outcome_asn = dict()

    def __init__(self, *args, verify_avoid_list=False, **kwargs):
        super(V4Scenario, self).__init__(*args, **kwargs)
        self.verify_avoid_list_flag = verify_avoid_list
        self.has_rovsms_ases = False

    def apply_blackholes_from_avoid_list(self, subgraphs):
        logger.debug(f"Inside apply_blackholes_from_avoid_list")
        # Create a flag to check if avoid_list has been created
        avoid_list_created_flag = False
        for subg_name, subgraph_asns in subgraphs.items():
            for asn in subgraph_asns:
                as_obj = self.engine.as_dict[asn]
                if hasattr(as_obj, "trusted_server"):
                    # Create the avoid list if it hasn't been created yet
                    if not avoid_list_created_flag:
                        self.trusted_server_ref = as_obj.trusted_server
                        as_obj.trusted_server.create_recs()
                        self.avoid_lists = self.trusted_server_ref._recommendations
                        avoid_list_created_flag = True
                        self.has_rovsms_ases = True

                    as_obj._force_add_blackholes_from_avoid_list(self.engine_input)

    def run(self, subgraphs, propagation_round: int):
        # Run engine
        self.engine.run(propagation_round=propagation_round,
                        engine_input=self.engine_input)
        # Add blackholes from avoid list
        self.apply_blackholes_from_avoid_list(subgraphs)
        # Calculate outcomes
        traceback_outcomes = self._collect_data(subgraphs)
        # Check if we need to verify the avoid_list
        if self.verify_avoid_list_flag and self.has_rovsms_ases:
            self.verify_avoid_list(traceback_outcomes)
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
        # Emtpy the trusted server
        if self.trusted_server_ref:
            self.trusted_server_ref.reset()
            # Note the trusted_server_ref is set inside apply_blackholes_from_avoid_list
            self.trusted_server_ref = None
        # Clear the outcomes dict
        del V4Scenario.traceback_outcome_asn
        V4Scenario.traceback_outcome_asn = dict()
        # Delete saved avoid list
        self.avoid_lists = None
        # Force garbage collection
        gc.collect()

        return traceback_outcomes

    def _get_outcomes(self, policies, countable_asns, cache):
        outcomes = {x: {y: 0 for y in policies}
                    for x in list(Outcomes)}
        # Most specific to least specific
        ordered_prefixes = self._get_ordered_prefixes()

        for asn in countable_asns:
            as_obj = self.engine.as_dict[asn]
            # Get the attack outcome
            outcome, traceback_asn = self._get_atk_outcome(as_obj, ordered_prefixes, 0, cache)
            # Incriment the outcome and policy by 1
            outcomes[outcome][as_obj.name] += 1
        return outcomes

    def _get_atk_outcome(self, as_obj, ordered_prefixes, path_len, cache):
        assert path_len < 128, "Path is too long, probably looping"

        if as_obj.asn in cache:
            return cache[as_obj.asn], self.traceback_outcome_asn[as_obj.asn]

        # Get most specific announcement, or empty RIB
        most_specific_ann = self._get_most_specific_ann(as_obj,
                                                        ordered_prefixes)
        # Determine the outcome of the attack
        attack_outcome, traceback_asn = self.engine_input.determine_outcome(as_obj,
                                                                            most_specific_ann)
        if not attack_outcome:
            # Continue tracing back by getting the last AS
            new_as_obj = self.engine.as_dict[most_specific_ann.as_path[1]]
            if not isinstance(as_obj, BGPAS):
                msg = ("Path manipulation not allowed for BGPSimpleAS. "
                       "Consider inheriting from BGPAS instead")
                assert new_as_obj in as_obj.neighbors, msg
            attack_outcome, traceback_asn = self._get_atk_outcome(new_as_obj,
                                                                  ordered_prefixes,
                                                                  path_len + 1,
                                                                  cache)
            msg = "Path manipulation attack with no traceback end?"
            assert (attack_outcome is not None
                    or new_as_obj in as_obj.neighbors)

        assert attack_outcome is not None, "Attack should be disconnected?"

        cache[as_obj.asn] = attack_outcome
        self.traceback_outcome_asn[as_obj.asn] = traceback_asn

        return attack_outcome, traceback_asn

    def verify_avoid_list(self, trackback_outcomes):
        """
        Makes sure that all the members of the avoid list 'does not lead victim'.
        (This satisfies the check that all members of the avoid list 'lead to
        the attacker'; which may not necessariy always happen if disconnecitions
        are created due to V4 or other reasons).
        :param trackback_outcomes:
        :return:
        """
        # Check that the avoid list ASes always lead to attacker
        # print(trackback_outcomes)
        for asn in self.avoid_lists[self.engine_input.attacker_prefix]:
            # TODO: Figure out why using the enum doesn't work
            # TODO: For some reason it literally prints "ASNs.Attacker"
            # print(f"Attacker: {enums.ASNs.ATTACKER}")
            # print(f"Victim: {enums.ASNs.VICTIM}")
            # TODO: The following commented out conditional doesn't work because above TODO
            # if asn != enums.ASNs.ATTACKER and asn != enums.ASNs.VICTIM:
            if asn != 666 and asn != 777:
                # print(asn)  # TODO: you can also see that 666 slips through
                if asn in trackback_outcomes:
                    assert trackback_outcomes[asn] != enums.Outcomes.VICTIM_SUCCESS, \
                        f"ASN: {asn} in avoid list leads to victim"
                    # Check if the disconnected case is not caused by a blackhole
                    as_obj = self.engine.as_dict[self.traceback_outcome_asn[asn]]
                    # TODO: the following check wouldn't work for v2, v2a, and v3
                    if trackback_outcomes[asn] == enums.Outcomes.DISCONNECTED \
                            and not (isinstance(as_obj, ROVPPV1SimpleAS)
                                     or isinstance(as_obj, ROVPPV1LiteSimpleAS)):
                        assert f"ASN: {asn} in avoid list was disconnected, but not by a blackhole."
