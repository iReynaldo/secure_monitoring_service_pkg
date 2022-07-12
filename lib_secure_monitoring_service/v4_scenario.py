import csv
from collections import defaultdict

from lib_bgp_simulator.simulator.scenario import Scenario
from lib_bgp_simulator.enums import Outcomes
from lib_bgp_simulator.engine import BGPAS

from lib_secure_monitoring_service.sim_logger import sim_logger as logger
from lib_secure_monitoring_service import metadata_collector

class V4Scenario(Scenario):
    trusted_server_ref = None
    outcomes_asn_cache = None
    outcomes = None

    def apply_blackholes_from_avoid_list(self, subgraphs):
        logger.debug(f"Inside apply_blackholes_from_avoid_list")
        # TODO: Delete the following lines once reports collected
        # -------------------------------------------------------------
        print("attacker_asn=", self.engine_input.attacker_asn)
        print("victim_asn=", self.engine_input.victim_asn)
        print("adopting_asns=", self.engine_input.adopting_asns)
        # -------------------------------------------------------------
        # Create a flag to check if avoid_list has been created
        avoid_list_created_flag = False
        header_written_flag = False  # TODO: Remove this flag once the following context is removed
        with open('as_metadata.tsv', 'a') as csvfile:  # TODO: Remove this context once done collecting AS metadata
            # TODO: Delete the following lines once reports collected
            # -------------------------------------------------------------
            fieldnames = [
                'percentAdoption', 'trial', 'asn', 'adopting', 'legitPrefixASPath', 'rank',
                'numPeers', 'numProviders', 'numCustomers', 'degree', 'subgraph', 'simAvoidList',
                'traceback_asn', 'victimASN', 'attackerASN', 'traceback_outcome'
            ]
            writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)
            # -------------------------------------------------------------
            for subg_name, subgraph_asns in subgraphs.items():
                for asn in subgraph_asns:
                    as_obj = self.engine.as_dict[asn]
                    # TODO: Delete the following lines once reports collected
                    # -------------------------------------------------------------
                    if as_obj.asn == self.engine_input.attacker_asn:
                        print("attacker_providers=", [aAs.asn for aAs in as_obj.providers])
                    is_adopting = False
                    # -------------------------------------------------------------
                    if hasattr(as_obj, "trusted_server"):
                        # Create the avoid list if it hasn't been created yet
                        if not avoid_list_created_flag:
                            self.trusted_server_ref = as_obj.trusted_server
                            as_obj.trusted_server.create_recs()
                            avoid_list_created_flag = True
                            # TODO: Delete the following lines once reports collected
                            # -------------------------------------------------------------
                            reports_path_list = list()
                            num_reports = 0
                            for prefix in as_obj.trusted_server._raw_data:
                                for report in as_obj.trusted_server._raw_data[prefix]:
                                    reports_path_list.append(list(report.as_path))
                                    num_reports += 1
                            print("reports_path_list=", reports_path_list)
                            print("num_reports=", num_reports)
                            # -------------------------------------------------------------

                        as_obj._force_add_blackholes_from_avoid_list(self.engine_input)
                    # TODO: Delete the following lines once reports collected
                    # -------------------------------------------------------------
                    prefix_ann = as_obj._local_rib.get_ann(prefix='1.2.0.0/16')
                    as_path = None
                    if prefix_ann:
                        as_path = list(prefix_ann.as_path)
                    numPeers = len(as_obj.peers)
                    numProviders = len(as_obj.providers)
                    numCustomers = len(as_obj.customers)
                    current_avoid_list = list(
                        self.trusted_server_ref._recommendations['1.2.3.0/24']) if self.trusted_server_ref else None
                    traceback_asn = self.outcomes_asn_cache.get(as_obj.asn, None)
                    traceback_outcome = self.outcomes.get(as_obj.asn, None)
                    victimASN = self.engine_input.victim_asn
                    attackerASN = self.engine_input.attacker_asn
                    row = {
                        'percentAdoption': metadata_collector.cur_percent_adoption,
                        'trial': metadata_collector.cur_trial,
                        'asn': as_obj.asn,
                        'adopting': is_adopting,
                        'legitPrefixASPath': as_path,
                        'rank': as_obj.propagation_rank,
                        'numPeers': numPeers,
                        'numProviders': numProviders,
                        'numCustomers': numCustomers,
                        'degree': numPeers + numProviders + numCustomers,
                        'subgraph': subg_name,
                        'simAvoidList': current_avoid_list,
                        'traceback_asn': traceback_asn,
                        'victimASN': victimASN,
                        'attackerASN': attackerASN,
                        'traceback_outcome': traceback_outcome
                    }
                    writer.writerow(row)
                    # -------------------------------------------------------------

    def run(self, subgraphs, propagation_round: int):
        # Run engine
        self.engine.run(propagation_round=propagation_round,
                        engine_input=self.engine_input)
        # Calculate outcomes
        traceback_outcomes, outcomes_asn_cache = self._collect_data(subgraphs)
        self.outcomes_asn_cache = outcomes_asn_cache
        self.outcomes = traceback_outcomes
        print("outcomes_asn_cache=", outcomes_asn_cache)
        # Add blackholes from avoid list
        self.apply_blackholes_from_avoid_list(subgraphs)
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
        # Wipe the outcomes_asn_cache
        outcomes_asn_cache = dict()

        return traceback_outcomes

    def _collect_data(self, subgraphs):
        """Collects data about the test run before engine is deleted"""

        policies = set([x.name for x in self.engine])
        cache = dict()
        outcomes_asn_cache = dict()

        # {subgraph_name: {outcome: {policy: percentage}}}
        self.outcome_policy_percentages = dict()
        for subg_name, subgraph_asns in subgraphs.items():
            countable_asns = subgraph_asns.difference(
                self.engine_input.uncountable_asns)

            outcome_totals = self._get_outcomes(policies,
                                                countable_asns,
                                                cache,
                                                outcomes_asn_cache)
            total_ases = self._get_policy_totals(policies, countable_asns)

            percentage_outcomes = defaultdict(dict)
            for outcome in list(Outcomes):
                for policy in policies:
                    outcome_policy_total = outcome_totals[outcome][policy]

                    policy_total = total_ases[policy]

                    percentage = outcome_policy_total * 100 / policy_total
                    percentage_outcomes[outcome][policy] = percentage

            self.outcome_policy_percentages[subg_name] = percentage_outcomes
        return cache, outcomes_asn_cache

    def _get_outcomes(self, policies, countable_asns, cache, outcomes_asn_cache):
        outcomes = {x: {y: 0 for y in policies}
                    for x in list(Outcomes)}
        # Most specific to least specific
        ordered_prefixes = self._get_ordered_prefixes()

        for asn in countable_asns:
            as_obj = self.engine.as_dict[asn]
            # Get the attack outcome
            outcome, outcome_asn = self._get_atk_outcome(as_obj, ordered_prefixes, 0, cache, outcomes_asn_cache)
            # Incriment the outcome and policy by 1
            outcomes[outcome][as_obj.name] += 1
        return outcomes

    def _get_atk_outcome(self, as_obj, ordered_prefixes, path_len, cache, outcomes_asn_cache):
        assert path_len < 128, "Path is too long, probably looping"

        # TODO: Uncomment this once you have the traceback ASNs
        # if as_obj.asn in cache:
        #     return cache[as_obj.asn]

        # Get most specific announcement, or empty RIB
        most_specific_ann = self._get_most_specific_ann(as_obj,
                                                        ordered_prefixes)
        # Determine the outcome of the attack
        attack_outcome, outcome_asn = self.engine_input.determine_outcome(as_obj,
                                                                          most_specific_ann)
        if not attack_outcome:
            # Continue tracing back by getting the last AS
            new_as_obj = self.engine.as_dict[most_specific_ann.as_path[1]]
            if not isinstance(as_obj, BGPAS):
                msg = ("Path manipulation not allowed for BGPSimpleAS. "
                       "Consider inheriting from BGPAS instead")
                assert new_as_obj in as_obj.neighbors, msg
            attack_outcome, outcome_asn = self._get_atk_outcome(new_as_obj,
                                                                ordered_prefixes,
                                                                path_len + 1,
                                                                cache,
                                                                outcomes_asn_cache)
            msg = "Path manipulation attack with no traceback end?"
            assert (attack_outcome is not None
                    or new_as_obj in as_obj.neighbors)

        assert attack_outcome is not None, "Attack should be disconnected?"

        cache[as_obj.asn] = attack_outcome
        # print("traceback_asn=", outcome_asn)
        outcomes_asn_cache[as_obj.asn] = outcome_asn

        return attack_outcome, outcome_asn
