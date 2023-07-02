from typing import Dict, Any, Type, Tuple, List, Optional
import ipaddress
import sys
import csv

from caida_collector_pkg import AS

from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Subgraph
from bgp_simulator_pkg import Outcomes
from bgp_simulator_pkg import Announcement as Ann

from rovpp_pkg import ROVPPV1SimpleAS
from rovpp_pkg import ROVPPV1LiteSimpleAS

from secure_monitoring_service_pkg.simulation_framework.scenarios import SubprefixAutoImmuneScenario
from secure_monitoring_service_pkg.simulation_framework.scenarios import V4SubprefixHijackScenario
from secure_monitoring_service_pkg.simulation_framework.scenarios import ArtemisSubprefixHijackScenario
from secure_monitoring_service_pkg.simulation_framework.scenarios.v4_scenario import CDN_RELAY_SETTING

# from secure_monitoring_service_pkg.simulation_framework.sim_logger import metadata_logger
from secure_monitoring_service_pkg.simulation_framework import metadata_collector


# TODO: Delete after debugging is done
#  --------------------------------------------------------------------
def write_csv_file_header(csv_file_name, fieldnames, delimeter):
    # Write Header of CSV Files
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimeter)
        writer.writeheader()

# Fieldnames
AVOID_LIST_CSV_FIELDNAMES = ['trial', 'percentage', 'propagation_round',
                             'adoption_setting', 'prefix_for_outcome',
                             'attacker_asns', 'victim_asn', 'avoid_list_len', 'avoid_list']
RELAY_OUTCOMES_CSV_FIELDNAMES = ['trial', 'percentage', 'propagation_round',
                                 'adoption_setting', 'relay', 'relay_asn',
                                 'prefix_for_outcome', 'outcome_before_relay',
                                 'outcome_after_relay', 'available', 'victim_asn',
                                 'attacker_asns', 'tunneled_with', 'avoid_list']
CSV_FILE_DELIMITER = '\t'
HEADERS_WRITTEN = False
#  --------------------------------------------------------------------


class V4Subgraph(Subgraph):
    v4_subclasses = []

    def __init_subclass__(cls, *args, **kwargs):
        """This method essentially creates a list of all subclasses
        This is allows us to know all attackers that have been created
        """

        super().__init_subclass__(*args, **kwargs)
        cls.v4_subclasses.append(cls)
        names = [x.name for x in cls.v4_subclasses if x.name]
        assert len(set(names)) == len(names), f"Duplicate subgraph class names {names}"

    def __init__(self):
        super(V4Subgraph, self).__init__()
        # Metadata filenames
        self.AVOID_LIST_CSV_FILE_NAME = metadata_collector.base_path + '/' + metadata_collector.output_filename + '_avoid_list_metadata.csv'
        self.RELAY_OUTCOMES_CSV_FILE_NAME = metadata_collector.base_path + '/' + metadata_collector.output_filename + '_relay_outcomes_metadata.csv'
        global HEADERS_WRITTEN
        if not HEADERS_WRITTEN:
            # Write their headers
            write_csv_file_header(self.AVOID_LIST_CSV_FILE_NAME, AVOID_LIST_CSV_FIELDNAMES, CSV_FILE_DELIMITER)
            write_csv_file_header(self.RELAY_OUTCOMES_CSV_FILE_NAME, RELAY_OUTCOMES_CSV_FIELDNAMES, CSV_FILE_DELIMITER)
            HEADERS_WRITTEN = True

    def verify_avoid_list(self,
                          engine,
                          scenario,
                          outcomes,
                          shared_data,
                          traceback_asn_outcomes,
                          trigger_assert=True):
        """
        Makes sure that all the members of the avoid list 'don't lead to victim'
        (This satisfies the check that all members of the avoid list 'lead to
        the attacker'; which may not necessarily always happen if disconnections
        are created due to V4 or other reasons).
        :param engine:
        :param scenario:
        :param traceback_asn_outcomes:
        :param outcomes:
        :return:
        """

        # Counters
        num_ases_should_not_be_on_avoid_list = 0
        num_victim_providers_on_avoid_list = 0

        # Check that the avoid list ASes always lead to attacker
        # print(outcomes)
        for prefix in scenario.avoid_lists:
            for asn in scenario.avoid_lists[prefix]:
                if isinstance(scenario, SubprefixAutoImmuneScenario):
                    # Check if asn is a victim's provider
                    # Note: the keys of 'subprefixes' are the provider ASNs of victim
                    if asn in scenario.subprefixes:
                        num_victim_providers_on_avoid_list += 1
                # TODO: Test if the following condition actually works
                if asn not in scenario.attacker_asns and asn not in scenario.victim_asns:
                    assert asn not in scenario.attacker_asns, f"Attacker ASN {asn} shouldn't be checked in verify_avoid_list"
                    assert asn not in scenario.victim_asns, f"Attacker ASN {asn} shouldn't be checked in verify_avoid_list"
                    if asn in outcomes:
                        # Check if ASN leads to Victim
                        if outcomes[asn] != Outcomes.VICTIM_SUCCESS:
                            num_ases_should_not_be_on_avoid_list += 1
                            assert trigger_assert, \
                                f"ASN: {asn} in avoid list leads to victim"

                        # Check if the disconnected case is not caused by a blackhole
                        as_obj = engine.as_dict[traceback_asn_outcomes[asn]]
                        # TODO: Does this check need to be counted and/or checked for AutoImmune Attack?
                        # TODO: the following check wouldn't work for v2, v2a, and v3
                        if outcomes[asn] == Outcomes.DISCONNECTED \
                                and not (isinstance(as_obj, ROVPPV1SimpleAS)
                                         or isinstance(as_obj, ROVPPV1LiteSimpleAS)):
                            assert f"ASN: {asn} in avoid list was disconnected, but not by a blackhole."

        if isinstance(scenario, SubprefixAutoImmuneScenario):
            # Update shared_data
            shared_data["num_ases_should_not_be_on_avoid_list"] = num_ases_should_not_be_on_avoid_list
            shared_data["num_victim_providers_on_avoid_list"] = num_victim_providers_on_avoid_list
            shared_data["num_of_victim_providers"] = len(scenario.subprefixes)
            shared_data["size_of_avoid_list"] = len(scenario.avoid_lists)

    # MARK: New
    def aggregate_engine_run_data(self,
                                  shared_data: Dict[Any, Any],
                                  *,
                                  engine: SimulationEngine,
                                  percent_adopt: float,
                                  trial: int,
                                  scenario: Scenario,
                                  propagation_round: int):
        """Aggregates data after a single engine run

        Shared data is passed between subgraph classes and is
        mutable. This is done to speed up data aggregation, even
        though it is at the cost of immutability

        shared data is reset after every run

        shared_data ex:
        {stubs_hijacked: int,
         stubs_hijacked_total: int,
         stubs_hijacked_percentage: float,
         stubs_hijacked_adopting: int
         stubs_hijacked_adopting_total: int,
         stubs_hijacked_adopting_percentage: float,
         stubs_hijacked_non_adopting: int,
         stubs_hijacked_non_adopting_total: int
         stubs_hijacked_non_adopting_percentage: float,
         ...
         }

        self.data ex:
        {scenario_label: {percent_adopt: [percents]}}
        """
        # TODO: Remove after done collecting metadata
        # -----------------------------------------------------
        available_relays_by_prefix_outcomes = dict()
        disconnected_relays_by_prefix_outcomes = dict()
        relay_usage_by_prefix_outcomes = dict()
        before_relay_usage_outcome_by_prefix_outcomes = dict()
        # -----------------------------------------------------

        prefix_outcomes: Dict[str, Dict[AS, Outcomes]] = dict()
        for attacker_ann in scenario.get_attacker_announcements_for_origin():
            if not shared_data.get("set"):  # this gets set in __add_traceback_to_shared_data:
                # {as_obj: outcome}
                outcomes, traceback_asn_outcomes = \
                    self._get_engine_outcomes(engine, scenario, attacker_ann)
                if scenario.relay_asns and not isinstance(scenario, ArtemisSubprefixHijackScenario):
                    self._recalculate_outcomes_with_relays(scenario,
                                                           engine,
                                                           attacker_ann,
                                                           outcomes,
                                                           traceback_asn_outcomes,
                                                           shared_data,
                                                           available_relays_by_prefix_outcomes,
                                                           disconnected_relays_by_prefix_outcomes,
                                                           relay_usage_by_prefix_outcomes,
                                                           before_relay_usage_outcome_by_prefix_outcomes)

                prefix_outcomes[attacker_ann.prefix] = outcomes

                # Verify the Avoid List
                if scenario.has_rovsms_ases:
                    # Verify avoid list according to the scenario
                    if isinstance(scenario, SubprefixAutoImmuneScenario):
                        self.verify_avoid_list(engine,
                                               scenario,
                                               outcomes,
                                               shared_data,
                                               traceback_asn_outcomes,
                                               trigger_assert=False)
                    elif isinstance(scenario, V4SubprefixHijackScenario):
                        self.verify_avoid_list(engine,
                                               scenario,
                                               outcomes,
                                               shared_data,
                                               traceback_asn_outcomes)
        # Aggregate Outcomes
        self._add_traceback_to_shared_data(shared_data,
                                           engine,
                                           scenario,
                                           prefix_outcomes)

        prefix_with_minimum_successful_connections = self.get_prefix_with_minimum_successful_connections(scenario,
                                                                                                         shared_data)

        # TODO: Delete after done debugging
        #  ------------------------------------------------------------------------------------------------------------
        # TODO: Why is prefix_outcomes sometime empty ......? -- Answer is because we don't need to outcomes recalculate between subgraphs
        if prefix_outcomes:
            if scenario.trusted_server_ref:
                with open(self.AVOID_LIST_CSV_FILE_NAME, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=AVOID_LIST_CSV_FIELDNAMES, delimiter=CSV_FILE_DELIMITER)
                    avoid_list = scenario.trusted_server_ref._recommendations[prefix_with_minimum_successful_connections]
                    row = {
                        'trial': trial,
                        'percentage': percent_adopt,
                        'propagation_round': propagation_round,
                        'adoption_setting': scenario.AdoptASCls.name,
                        'prefix_for_outcome': prefix_with_minimum_successful_connections,
                        'attacker_asns': str(list(scenario.attacker_asns)),
                        'victim_asn': next(iter(scenario.victim_asns)),
                        'avoid_list_len': len(avoid_list),
                        'avoid_list': str(avoid_list)
                    }
                    writer.writerow(row)
                    csvfile.flush()
            if scenario.relay_asns:
                for relay_asn in scenario.relay_asns:
                    with open(self.RELAY_OUTCOMES_CSV_FILE_NAME, 'a') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=RELAY_OUTCOMES_CSV_FIELDNAMES, delimiter=CSV_FILE_DELIMITER)
                        key = f"{prefix_with_minimum_successful_connections}+{relay_asn}"
                        row = {
                            'trial': trial,
                            'percentage': percent_adopt,
                            'propagation_round': propagation_round,
                            'adoption_setting': scenario.AdoptASCls.name,
                            'prefix_for_outcome': prefix_with_minimum_successful_connections,
                            'attacker_asns': str(list(scenario.attacker_asns)),
                            'victim_asn': next(iter(scenario.victim_asns)),
                            'relay': scenario.relay_name,
                            'relay_asn': relay_asn,
                            'outcome_before_relay': before_relay_usage_outcome_by_prefix_outcomes[key],
                            'outcome_after_relay': prefix_outcomes[prefix_with_minimum_successful_connections][engine.as_dict[relay_asn]],
                            'available': relay_asn in available_relays_by_prefix_outcomes[prefix_with_minimum_successful_connections],
                            'tunneled_with': relay_usage_by_prefix_outcomes.get(key, None),
                            'avoid_list': str(
                                scenario.trusted_server_ref._recommendations[prefix_with_minimum_successful_connections])
                        }
                        writer.writerow(row)
                        csvfile.flush()
        # -------------------------------------------------------------------------------------------------------------

        key = self._get_subgraph_key(scenario)
        shared_data[key] = shared_data.get(key + f"_{prefix_with_minimum_successful_connections}", 0)
        self.data[propagation_round][scenario.graph_label][percent_adopt
        ].append(shared_data.get(key, 0))  # noqa

    def _as_has_blackhole_for_attack_on_origin_prefix(self, as_obj, attacker_prefix):
        # Check if created a blackhole
        attacker_ann_from_relay_local_rib = as_obj._local_rib.get_ann(attacker_prefix)
        if attacker_ann_from_relay_local_rib and attacker_ann_from_relay_local_rib.blackhole:
            return True
        return False

    def _relay_is_available(self, engine, scenario, attacker_prefix, relay_asn):
        """
        Checks if the relay ASN has a path to the legit origin
        AND
        Has not created a blackhole.
            Black holes are created from:
                - Direct observation of the hijack attempt
                - From avoid list
        :param relay_asn:
        :return: bool
        """
        as_obj = engine.as_dict[relay_asn]
        origin_prefix = next(iter(scenario.get_victim_announcements())).prefix
        # Check if relay has path to origin AND
        # does not have a blackhole for attacker's attack on the origin
        origin_ann = as_obj._local_rib.get_ann(origin_prefix)
        if origin_ann and \
                not self._as_has_blackhole_for_attack_on_origin_prefix(as_obj, attacker_prefix):
            if scenario.trusted_server_ref:
                # Check that the AS path for the origin prefix does not have any ASes that have blackholes
                ases_with_blackholes = scenario.trusted_server_ref.adopters_with_blackhole.get(attacker_prefix, None)
                if ases_with_blackholes:
                    for asn in origin_ann.as_path:
                        if asn in ases_with_blackholes:
                            return False
            return True
        else:
            return False

    def _recalculate_outcomes_with_relays(self, scenario, engine, attacker_ann,
                                          outcomes, traceback_asn_outcomes,
                                          shared_data,
                                          available_relays_by_prefix_outcomes,
                                          disconnected_relays_by_prefix_outcomes,
                                          relay_usage_by_prefix_outcomes,
                                          before_relay_usage_outcome_by_prefix_outcomes,
                                          track_relay_usage=False):
        """Mutate outcomes and traceback_asn_outcomes with potential reconnections
        from relays."""
        # This flag will indicate if re-computation of outcomes is necessary
        changes_made_flag = False
        # Create a set of relays that have successful connections to origin
        connected_relays = set()
        for relay_asn in scenario.relay_asns:
            if self._relay_is_available(engine, scenario, attacker_ann.prefix, relay_asn):
                connected_relays.add(relay_asn)
            before_relay_usage_outcome_by_prefix_outcomes[f"{attacker_ann.prefix}+{relay_asn}"] = outcomes[engine.as_dict[relay_asn]]

        available_relays_by_prefix_outcomes[attacker_ann.prefix] = connected_relays
        disconnected_relays_by_prefix_outcomes[attacker_ann.prefix] = scenario.relay_asns - connected_relays
        
        if len(connected_relays) > 0:
            # If the relay_setting is CDN, then if any one of the
            # the relay ASNs is avaialable, then all corresponding relay
            # ASNs are also available, as we can assume they can tunnel to each other
            not_connected_relay_as_obj = list()
            if scenario.relay_setting == CDN_RELAY_SETTING:
                for asn in scenario.relay_asns - connected_relays:
                    not_connected_relay_as_obj.append(engine.as_dict[asn])
            # For each adopting ASN (except relay), check if it's disconnected
            for as_obj_iterator in [not_connected_relay_as_obj, outcomes]:
                for as_obj in as_obj_iterator:
                    # TODO: Why doesn't issubclass(as_obj, ROVSMS) work here for Config150?
                    if hasattr(as_obj, "trusted_server") and \
                            outcomes[as_obj] == Outcomes.DISCONNECTED and \
                            as_obj.asn not in connected_relays:
                        if scenario.relay_setting != CDN_RELAY_SETTING:
                            selected_relay_asn = as_obj.use_relay(connected_relays,
                                                                  scenario.relay_prefixes,
                                                                  scenario.assume_relays_are_reachable)
                        else:
                            selected_relay_asn = as_obj.use_relay(connected_relays,
                                                                  scenario.relay_prefixes,
                                                                  True)
                        if selected_relay_asn:
                            relay_usage_by_prefix_outcomes[f"{attacker_ann.prefix}+{as_obj.asn}"] = selected_relay_asn
                            # Update outcome for asn to outcome of the Relay that was selected
                            outcomes[as_obj] = outcomes[engine.as_dict[selected_relay_asn]]
                            # Update traceback_asn_outcome to victim asn
                            traceback_asn_outcomes[as_obj.asn] = traceback_asn_outcomes[selected_relay_asn]
                            # Update flag to signal re-computation of outcomes
                            changes_made_flag = True
                            # Track which relays are being used
                            if track_relay_usage:
                                # Add ASN to set of ASes using the relay to shared_data
                                relay_usage = shared_data.get("relay_usage", dict())
                                relay_users = relay_usage.get(selected_relay_asn, set())
                                relay_users.add(as_obj.asn)
                                relay_usage[selected_relay_asn] = relay_users
                                shared_data["relay_usage"] = relay_usage
                # If relay setting is CDN, then they can tunnel between each other
                if scenario.relay_setting == CDN_RELAY_SETTING:
                    # After the first time through the inner loop,
                    # all the relays should be considered
                    # available, because their evaluated first.
                    connected_relays = scenario.relay_asns
            if scenario.tunnel_customer_traffic and changes_made_flag:
                self._get_engine_outcomes(engine, scenario, attacker_ann, outcomes, traceback_asn_outcomes, True)

    def get_prefix_with_minimum_successful_connections(self, scenario, shared_data):
        min_prefix = ""
        min_percentage = sys.maxsize
        for attacker_ann in scenario.get_attacker_announcements_for_origin():
            if attacker_ann.prefix not in scenario.relay_prefixes.values():
                # This string must match up to "_perc_" with the one in victim_success_all_subgraph.py
                subgraph_key = f"all_{Outcomes.VICTIM_SUCCESS.name}_perc_{attacker_ann.prefix}"
                if shared_data[subgraph_key] < min_percentage:
                    min_percentage = shared_data[subgraph_key]
                    min_prefix = attacker_ann.prefix
        return min_prefix

    # MARK: New
    def _get_as_outcome(self,
                        as_obj: AS,
                        outcomes: Dict[AS, Outcomes],
                        traceback_asn_outcomes: Dict[int, int],
                        engine: SimulationEngine,
                        scenario: Scenario,
                        attacker_ann: Ann,
                        force_recompute: bool = False
                        ) -> Tuple[Type[Outcomes], Type[int]]:
        """Recursively returns the as outcome"""
        if force_recompute and as_obj in outcomes and outcomes[as_obj] != Outcomes.DISCONNECTED:
            return outcomes[as_obj], traceback_asn_outcomes[as_obj.asn]
        if not force_recompute and as_obj in outcomes:
            return outcomes[as_obj], traceback_asn_outcomes[as_obj.asn]
        else:
            # Get the most specific announcement in the rib
            most_specific_ann = self._get_most_specific_ann(
                as_obj, scenario.ordered_prefix_subprefix_dict, attacker_ann)
            # This has to be done in the scenario
            # Because only the scenario knows attacker/victim
            # And it's possible for scenario's to have multiple attackers
            # or multiple victims or different ways of determining outcomes
            outcome, traceback_asn = scenario.determine_as_outcome(as_obj, most_specific_ann)
            # We haven't traced back all the way on the AS path
            if outcome == Outcomes.UNDETERMINED:
                # next as in the AS path to traceback to
                # Ignore type because only way for this to be here
                # Is if the most specific Ann was NOT None.
                next_as = engine.as_dict[
                    most_specific_ann.as_path[1]  # type: ignore
                ]  # type: ignore
                outcome, traceback_asn = self._get_as_outcome(next_as,
                                                              outcomes,
                                                              traceback_asn_outcomes,
                                                              engine,
                                                              scenario,
                                                              attacker_ann,
                                                              force_recompute)
            assert outcome != Outcomes.UNDETERMINED, "Shouldn't be possible"

            outcomes[as_obj] = outcome
            traceback_asn_outcomes[as_obj.asn] = traceback_asn
            return outcome, traceback_asn

    def _get_most_specific_ann(self,
                               as_obj: AS,
                               ordered_prefixes: Dict[str, List[str]],
                               attacker_ann: Ann
                               ) -> Optional[Ann]:
        """Returns the most specific announcement that exists in a rib

        as_obj is the as
        ordered prefixes are prefixes ordered from most specific to least
        """

        attacker_ann_prefix = ipaddress.ip_network(attacker_ann.prefix)
        for prefix in ordered_prefixes:
            if attacker_ann_prefix.subnet_of(ipaddress.ip_network(prefix)):
                most_specific_ann = as_obj._local_rib.get_ann(prefix)
                if most_specific_ann:
                    # Mypy doesn't recognize that this is always an annoucnement
                    return most_specific_ann  # type: ignore
        return None

    # MARK: New
    def _get_engine_outcomes(self,
                             engine: SimulationEngine,
                             scenario: Scenario,
                             attacker_ann: Ann,
                             outcomes: dict = None,
                             traceback_asn_outcomes: dict = None,
                             recompute_disconnections: bool = False) -> Tuple[Dict[AS, Outcomes], Dict[int, int]]:
        """Gets the outcomes of all ASes"""

        # {ASN: outcome}
        outcomes: Dict[AS, Outcomes] = outcomes if outcomes else dict()
        traceback_asn_outcomes: Dict[int, int] = traceback_asn_outcomes if traceback_asn_outcomes else dict()
        for as_obj in engine.as_dict.values():
            if recompute_disconnections and outcomes[as_obj] == Outcomes.DISCONNECTED:
                # Gets AS outcome and stores it in the outcomes dict
                self._get_as_outcome(as_obj,
                                     outcomes,
                                     traceback_asn_outcomes,
                                     engine,
                                     scenario,
                                     attacker_ann,
                                     force_recompute=True)
            else:
                # Gets AS outcome and stores it in the outcomes dict
                self._get_as_outcome(as_obj,
                                     outcomes,
                                     traceback_asn_outcomes,
                                     engine,
                                     scenario,
                                     attacker_ann)
        return outcomes, traceback_asn_outcomes

    def _add_traceback_to_shared_data(self,
                                      shared: Dict[Any, Any],
                                      engine: SimulationEngine,
                                      scenario: Scenario,
                                      prefix_outcomes: Dict[str, Dict[AS, Outcomes]]):
        """Adds traceback info to shared data"""

        counted_group_size = False  # Flag to not recalculate AS-group (i.e. etc, input clique, edge) size
        for prefix, outcomes in prefix_outcomes.items():
            for as_obj, outcome in outcomes.items():
                as_type = self._get_as_type(as_obj)

                # TODO: refactor this ridiculousness into a class
                # Add to the AS type and policy, as well as the outcome
                # THESE ARE JUST KEYS, JUST GETTING KEYS/Strings HERE
                ##################################################################
                as_type_pol_k = self._get_as_type_pol_k(as_type, as_obj.__class__)
                as_type_pol_prefix_outcome_k = self._get_as_type_pol_prefix_outcome_k(
                    as_type, as_obj.__class__, prefix, outcome,
                )
                ##################################################################

                # Add to the totals:
                for k in [as_type_pol_k, as_type_pol_prefix_outcome_k]:
                    if k == as_type_pol_k:
                        if not counted_group_size:
                            shared[k] = shared.get(k, 0) + 1
                    else:
                        shared[k] = shared.get(k, 0) + 1

                ############################
                # Track stats for all ASes #
                ############################

                # Keep track of totals for all ASes
                name = outcome.name
                total = shared.get(f"all_{name}_{prefix}", 0) + 1
                shared[f"all_{name}_{prefix}"] = total

            # Set group size as calculated, so it doesn't continue to increase with next prefix
            counted_group_size = True

        # Must calculate percentages at the end
        # NOTE: this double for loop should realy be avoided
        # Only O(2n) but bad for runtime
        for prefix, outcomes in prefix_outcomes.items():
            for as_obj, outcome in outcomes.items():
                as_type = self._get_as_type(as_obj)
                as_type_pol_k = self._get_as_type_pol_k(as_type, as_obj.__class__)
                as_type_pol_prefix_outcome_k = self._get_as_type_pol_prefix_outcome_k(
                    as_type, as_obj.__class__, prefix, outcome,
                )
                # as type + policy + outcome as a percentage
                as_type_pol_prefix_outcome_perc_k = self._get_as_type_pol_prefix_outcome_perc_k(
                    as_type, as_obj.__class__, prefix, outcome
                )
                # Set the new percent
                if shared.get(as_type_pol_prefix_outcome_k) is not None:
                    shared[as_type_pol_prefix_outcome_perc_k] = (
                            shared[as_type_pol_prefix_outcome_k] *
                            100 / shared[as_type_pol_k]
                    )
                name = outcome.name
                total = shared[f"all_{name}_{prefix}"]
                # Keep track of percentages for all ASes
                shared[f"all_{name}_perc_{prefix}"] = total * 100 / len(outcomes)

        shared["set"] = True

    def _get_as_type_pol_prefix_outcome_k(self,
                                          as_type: Any,
                                          ASCls: Type[AS],
                                          prefix: str,
                                          outcome: Outcomes) -> str:
        """returns as type+policy+outcome key"""
        x = self._get_as_type_pol_outcome_k(as_type, ASCls, outcome)
        return f"{x}_{prefix}"

    def _get_as_type_pol_prefix_outcome_perc_k(self,
                                               as_type: Any,
                                               ASCls: Type[AS],
                                               prefix: str,
                                               outcome: Outcomes) -> str:
        """returns as type+policy+outcome key as a percent"""

        x = self._get_as_type_pol_outcome_perc_k(as_type, ASCls, outcome)
        return f"{x}_{prefix}"
