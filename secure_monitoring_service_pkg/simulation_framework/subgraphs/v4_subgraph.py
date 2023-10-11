from typing import Dict, Any, Type, Tuple, List, Optional
import ipaddress
import sys
import csv
from collections import Counter

from filelock import FileLock

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
from secure_monitoring_service_pkg.simulation_engine.as_classes import ROVPPO
from secure_monitoring_service_pkg.simulation_engine.as_classes import ROVSMS
from secure_monitoring_service_pkg.simulation_framework import metadata_collector


class V4Subgraph(Subgraph):
    v4_subclasses = []

    # metadata collection variables
    available_relay_counter_key = 'available'
    relay_usage_edge_counter_key = 'edge_usage'
    relay_usage_etc_counter_key = 'etc_usage'
    relay_usage_clique_counter_key = 'clique_usage'
    outcome_map = {
        Outcomes.ATTACKER_SUCCESS: 'hijacked',
        Outcomes.VICTIM_SUCCESS: 'successful',
        Outcomes.DISCONNECTED: 'disconnected',
        Outcomes.UNDETERMINED: 'undetermined'
    }

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
        # Variables for metadata collection
        self.csv_file_delimiter = metadata_collector.CSV_FILE_DELIMITER
        # Avoid list metadata variables
        self.collect_avoid_list_metadata = metadata_collector.collect_avoid_list_metadata
        self.avoid_list_csv_filename = metadata_collector.avoid_list_csv_filename
        self.avoid_list_metadata_fieldnames = metadata_collector.AVOID_LIST_CSV_FIELDNAMES
        # AS metadata variables
        self.collect_as_metadata = metadata_collector.collect_as_metadata
        self.as_csv_filename = metadata_collector.as_csv_filename
        self.as_metadata_fieldnames = metadata_collector.AS_CSV_FIELDNAMES
        # Aggregate AS metadata variables
        self.collect_agg_as_metadata = metadata_collector.collect_agg_as_metadata
        self.agg_as_csv_filename = metadata_collector.agg_as_csv_filename
        self.agg_as_metadata_fieldnames = metadata_collector.AGG_AS_CSV_FIELDNAMES


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

        # Metadata tracking variables
        before_relay_usage = Counter()
        after_relay_usage = Counter()

        prefix_outcomes: Dict[str, Dict[AS, Outcomes]] = dict()
        for attacker_ann in scenario.get_attacker_announcements_for_origin():
            if not shared_data.get("set"):  # this gets set in __add_traceback_to_shared_data:
                # {as_obj: outcome}
                outcomes, traceback_asn_outcomes = \
                    self._get_engine_outcomes(engine, scenario, attacker_ann)
                if scenario.relay_asns and not isinstance(scenario, ArtemisSubprefixHijackScenario):
                    self._recalculate_outcomes_with_relays(scenario, engine, attacker_ann, outcomes,
                                                           traceback_asn_outcomes, shared_data,
                                                           before_relay_usage=before_relay_usage,
                                                           after_relay_usage=after_relay_usage)

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

        # Why is prefix_outcomes sometime empty? -- Answer is because we don't need to outcomes recalculate between subgraphs
        if self.collect_avoid_list_metadata and prefix_outcomes:
            if scenario.trusted_server_ref:
                self.write_avoid_list_metadata(
                    trial, percent_adopt, propagation_round,
                    scenario, prefix_with_minimum_successful_connections,
                    before_relay_usage, after_relay_usage)

        if self.collect_as_metadata and prefix_outcomes:
            self.write_as_metadata(
                trial, percent_adopt, propagation_round,
                scenario,
                prefix_with_minimum_successful_connections,
                prefix_outcomes[prefix_with_minimum_successful_connections])

        if self.collect_agg_as_metadata and prefix_outcomes:
            self.write_agg_as_metadata(
                 trial, percent_adopt, propagation_round,
                 scenario,
                 prefix_with_minimum_successful_connections,
                 prefix_outcomes[prefix_with_minimum_successful_connections])

        key = self._get_subgraph_key(scenario)
        shared_data[key] = shared_data.get(key + f"_{prefix_with_minimum_successful_connections}", 0)
        self.data[propagation_round][scenario.graph_label][percent_adopt
        ].append(shared_data.get(key, 0))  # noqa

    def write_avoid_list_metadata(self, trial, percent_adopt, propagation_round,
                                    scenario, prefix,
                                    before_relay_usage, after_relay_usage):
        with metadata_collector.avoid_list_csv_flock:
            with open(self.avoid_list_csv_filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile,
                                        fieldnames=self.avoid_list_metadata_fieldnames,
                                        delimiter=self.csv_file_delimiter)
                avoid_list = scenario.trusted_server_ref._recommendations[
                    prefix]
                # Calculate some CSV features
                num_relay_asns = 0 if not scenario.relay_asns else len(scenario.relay_asns)
                # Create new row
                row = {
                    'trial': trial,
                    'percentage': percent_adopt,
                    'propagation_round': propagation_round,
                    'adoption_setting': scenario.AdoptASCls.name,
                    'prefix_for_outcome': prefix,
                    'attacker_asns': str(list(scenario.attacker_asns)),
                    'victim_asn': next(iter(scenario.victim_asns)),
                    'relay_name': scenario.relay_name,
                    'num_relays': num_relay_asns,
                    'edge_using_relay': after_relay_usage[self.relay_usage_edge_counter_key],
                    'etc_using_relay': after_relay_usage[self.relay_usage_etc_counter_key],
                    'input_clique_using_relay': after_relay_usage[self.relay_usage_clique_counter_key],
                    'before_relay_num_relays_hijacked': before_relay_usage[Outcomes.ATTACKER_SUCCESS],
                    'before_relay_num_relays_victim_success': before_relay_usage[Outcomes.VICTIM_SUCCESS],
                    'before_relay_num_relays_disconnected': before_relay_usage[Outcomes.DISCONNECTED],
                    'before_relay_num_relays_available': before_relay_usage[self.available_relay_counter_key],
                    'after_relay_num_relays_hijacked': after_relay_usage[Outcomes.ATTACKER_SUCCESS],
                    'after_relay_num_relays_victim_success': after_relay_usage[Outcomes.VICTIM_SUCCESS],
                    'after_relay_num_relays_disconnected': after_relay_usage[Outcomes.DISCONNECTED],
                    'after_relay_num_relays_available': after_relay_usage[self.available_relay_counter_key],
                    'avoid_list_len': len(avoid_list),
                    'avoid_list': str(avoid_list) if len(avoid_list) else '{}'
                }
                writer.writerow(row)

    def write_as_metadata(self, trial, percent_adopt, propagation_round,
                          scenario, prefix, outcomes):
        with metadata_collector.as_csv_flock:
            with open(self.as_csv_filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile,
                                        fieldnames=self.as_metadata_fieldnames,
                                        delimiter=self.csv_file_delimiter)
                # Calculate some CSV features
                for as_obj, outcome in outcomes.items():
                    # Get values for features
                    # Used Relay feature
                    used_relay = self._calc_used_relay(as_obj)
                    # Number of Adopting Providers & Using Adopting Provider
                    num_adopting_providers, using_adopting_provider = \
                        self._calc_adopting_provider_features(as_obj, scenario, prefix)
                    # Create new row
                    row = {
                        'trial': trial,
                        'percentage': percent_adopt,
                        'propagation_round': propagation_round,
                        'adoption_setting': scenario.AdoptASCls.name,
                        'prefix_for_outcome': prefix,
                        'attacker_asns': str(list(scenario.attacker_asns)),
                        'victim_asn': next(iter(scenario.victim_asns)),
                        'relay_name': scenario.relay_name,
                        'asn': as_obj.asn,
                        'policy': as_obj.name,
                        'num_providers': len(as_obj.providers),
                        'num_adopting_providers': num_adopting_providers,
                        'outcome': outcome,
                        'using_adopting_provider': using_adopting_provider,
                        'using_relay': used_relay
                    }
                    writer.writerow(row)

    def write_agg_as_metadata(self, trial, percent_adopt, propagation_round,
                              scenario, prefix, outcomes):
        with metadata_collector.agg_as_csv_flock:
            with open(self.agg_as_csv_filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile,
                                        fieldnames=self.agg_as_metadata_fieldnames,
                                        delimiter=self.csv_file_delimiter)
                # Calculate features
                # Get counts
                counts = Counter()
                for as_obj, outcome in outcomes.items():
                    adoption_setting = 'ad' if as_obj.name == scenario.AdoptASCls.name else 'nonad'
                    provider_setting, using_adopting_provider_setting = self._provider_setting(as_obj, scenario, prefix)
                    topology_section = self._topology_section(as_obj)
                    outcome = self.outcome_map[outcome]
                    counts['_'.join([adoption_setting, provider_setting,
                                    using_adopting_provider_setting, topology_section, outcome])] += 1
                    # For any topology section (i.e. all) add to it
                    counts['_'.join([adoption_setting, provider_setting,
                                     using_adopting_provider_setting, 'all', outcome])] += 1
                # Create new row
                row = {
                    'trial': trial,
                    'percentage': percent_adopt,
                    'propagation_round': propagation_round,
                    'adoption_setting': scenario.AdoptASCls.name,
                    'prefix_for_outcome': prefix,
                    'attacker_asns': str(list(scenario.attacker_asns)),
                    'victim_asn': next(iter(scenario.victim_asns)),
                    'relay_name': scenario.relay_name
                }
                row.update(counts)
                writer.writerow(row)

    def _provider_setting(self, as_obj, scenario, prefix):
        # Used Relay feature
        used_relay = self._calc_used_relay(as_obj)
        # Numer of Adopting Providers & Using Adopting Provider
        num_adopting_providers, using_adopting_provider = \
            self._calc_adopting_provider_features(as_obj, scenario, prefix)
        using_adopting_provider_setting = 'using' if using_adopting_provider else 'notusing'
        num_proivders = len(as_obj.providers)
        if num_adopting_providers == 0:
            return 'noad', using_adopting_provider_setting
        elif 0 < num_adopting_providers < num_proivders:
            return 'al1ad', using_adopting_provider_setting
        elif num_adopting_providers == num_proivders:
            return 'allad', using_adopting_provider_setting

    def _topology_section(self, as_obj):
        if as_obj.stub or as_obj.multihomed:
            return 'edge'
        elif as_obj.input_clique:
            return 'clique'
        else:
            return 'etc'

    def _calc_used_relay(self, as_obj):
        used_relay = None
        if isinstance(as_obj, ROVPPO) or isinstance(as_obj, ROVSMS):
            used_relay = as_obj.used_relay
        return used_relay

    def _calc_adopting_provider_features(self, as_obj, scenario, prefix):
        most_specific_ann = self._get_most_specific_ann(
            as_obj, scenario.ordered_prefix_subprefix_dict, prefix)
        most_specific_ann_as_path = None
        if most_specific_ann:
            most_specific_ann_as_path = most_specific_ann.as_path
        using_adopting_provider = False
        num_adopting_providers = 0
        for provider_as_obj in as_obj.providers:
            if isinstance(provider_as_obj, scenario.AdoptASCls):
                num_adopting_providers += 1
                if most_specific_ann_as_path and provider_as_obj.asn in most_specific_ann_as_path:
                    using_adopting_provider = True
        return num_adopting_providers, using_adopting_provider

    def _as_has_blackhole_for_attack_on_origin_prefix(self, as_obj, attacker_prefix):
        # Check if created a blackhole
        attacker_ann_from_relay_local_rib = as_obj._local_rib.get_ann(attacker_prefix)
        if attacker_ann_from_relay_local_rib and attacker_ann_from_relay_local_rib.blackhole:
            return True
        return False

    def _relay_is_available(self, engine, scenario, outcomes, attacker_prefix, relay_asn):
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
        if scenario.probe_data_plane:
            return outcomes[engine.as_dict[relay_asn]] == Outcomes.VICTIM_SUCCESS
        else:
            as_obj = engine.as_dict[relay_asn]
            origin_prefix = next(iter(scenario.get_victim_announcements())).prefix
            # Check if relay has path to origin AND
            # does not have a blackhole for attacker's attack on the origin
            origin_ann = as_obj._local_rib.get_ann(origin_prefix)
            if origin_ann and \
                    not self._as_has_blackhole_for_attack_on_origin_prefix(as_obj, attacker_prefix):
                if scenario.trusted_server_ref:
                    # Check that the AS path for the origin prefix does not have any ASes that have blackholes
                    ases_with_blackholes = scenario.trusted_server_ref.adopters_with_blackhole.get(attacker_prefix,
                                                                                                   None)
                    if ases_with_blackholes:
                        for asn in origin_ann.as_path:
                            if asn in ases_with_blackholes:
                                return False
                return True
            else:
                return False

    def has_access_to_relay_service(self, as_obj) -> bool:
        """Returns a boolean stating if a AS Object has access to the relay service"""
        if "ROV V4 Lite" in as_obj.name or "Overlayed" in as_obj.name:
            return True
        else:
            return False

    def _recalculate_outcomes_with_relays(self, scenario, engine, attacker_ann, outcomes, traceback_asn_outcomes,
                                          shared_data,
                                          before_relay_usage=None,
                                          after_relay_usage=None,
                                          track_relay_usage=False):
        """Mutate outcomes and traceback_asn_outcomes with potential reconnections
        from relays."""
        # Create Bogus Counters in the case their not specified
        if before_relay_usage is None:
            before_relay_usage = Counter()
        if after_relay_usage is None:
            after_relay_usage = Counter()

        # This flag will indicate if re-computation of outcomes is necessary
        changes_made_flag = False

        # Create a set of relays that have successful connections to origin
        available_relays = set()
        if ROVPPO.__name__ == scenario.AdoptASCls.__name__ and not scenario.probe_data_plane:
            # If the adopting ASes are running ROV++ Overlay
            # without the ability to probe the dataplane, then there is
            # no way to filter the available Relays. So simply say all
            # relays are available to use.
            available_relays = scenario.relay_asns
            # Update Metadata tracking variable
            before_relay_usage.update((self.available_relay_counter_key,) * len(available_relays))
        else:
            for relay_asn in scenario.relay_asns:
                if self._relay_is_available(engine, scenario, outcomes, attacker_ann.prefix, relay_asn):
                    available_relays.add(relay_asn)
            # Update Metadata tracking variable
            before_relay_usage.update((self.available_relay_counter_key,) * len(available_relays))

        # If the relay_setting is CDN, then if any one of the
        # relay ASNs is available, then all corresponding relay
        # ASNs are also available, as we can assume they can tunnel to each other
        not_connected_relay_as_obj = list()
        if scenario.relay_setting == CDN_RELAY_SETTING:
            for asn in scenario.relay_asns - available_relays:
                not_connected_relay_as_obj.append(engine.as_dict[asn])

        seen_relay_ases = set()

        if len(available_relays) > 0:
            # For each adopting ASN (except relay), check if it's disconnected
            for as_obj_iterator in [not_connected_relay_as_obj, outcomes]:
                for as_obj in as_obj_iterator:
                    # Update Metadata tracking variable
                    if as_obj.asn in scenario.relay_asns and as_obj.asn not in seen_relay_ases:
                        before_relay_usage.update((outcomes[as_obj],))
                    if self.has_access_to_relay_service(as_obj) and \
                            outcomes[as_obj] != Outcomes.VICTIM_SUCCESS and \
                            as_obj.asn not in available_relays:
                        if as_obj.asn in scenario.relay_asns and scenario.relay_setting == CDN_RELAY_SETTING:
                            selected_relay_asn = as_obj.use_relay(available_relays,
                                                                  scenario.relay_prefixes,
                                                                  True)
                        else:
                            selected_relay_asn = as_obj.use_relay(available_relays,
                                                                  scenario.relay_prefixes,
                                                                  scenario.assume_relays_are_reachable)
                        if selected_relay_asn:
                            # Update the ASes relay usage variable
                            as_obj.used_relay = True
                            # Update outcome for asn to outcome of the Relay that was selected
                            outcomes[as_obj] = outcomes[engine.as_dict[selected_relay_asn]]
                            # Update traceback_asn_outcome to victim asn
                            traceback_asn_outcomes[as_obj.asn] = traceback_asn_outcomes[selected_relay_asn]
                            # Update flag to signal re-computation of outcomes
                            changes_made_flag = True
                            # Update Metadata tracking variables
                            if as_obj.stub or as_obj.multihomed:
                                after_relay_usage.update((self.relay_usage_edge_counter_key,))
                            elif as_obj.input_clique:
                                after_relay_usage.update((self.relay_usage_clique_counter_key,))
                            else:
                                after_relay_usage.update((self.relay_usage_etc_counter_key,))
                            # Track which relays are being used
                            if track_relay_usage:
                                # Add ASN to set of ASes using the relay to shared_data
                                relay_usage = shared_data.get("relay_usage", dict())
                                relay_users = relay_usage.get(selected_relay_asn, set())
                                relay_users.add(as_obj.asn)
                                relay_usage[selected_relay_asn] = relay_users
                                shared_data["relay_usage"] = relay_usage
                    # Update Metadata tracking variable
                    if as_obj.asn in scenario.relay_asns and as_obj.asn not in seen_relay_ases:
                        after_relay_usage.update((outcomes[as_obj],))
                        # Update seen relay ASNs
                        seen_relay_ases.add(as_obj.asn)
                # If relay setting is CDN, then they can tunnel between each other
                if scenario.relay_setting == CDN_RELAY_SETTING:
                    # After the first time through the inner loop,
                    # all the relays should be considered
                    # available, because their evaluated first.
                    available_relays = scenario.relay_asns
            if scenario.tunnel_customers_traffic and changes_made_flag:
                self._get_engine_outcomes(engine, scenario, attacker_ann, outcomes, traceback_asn_outcomes, True)
        else:
            # If there's no option to connect to relay and the ASes outcome is
            # ATTAKCER_SUCCESS, then the AS should simply disconnect if probing is enabled
            for as_obj_iterator in [not_connected_relay_as_obj, outcomes]:
                for as_obj in as_obj_iterator:
                    if self.has_access_to_relay_service(as_obj) and \
                            outcomes[as_obj] == Outcomes.ATTACKER_SUCCESS and \
                            as_obj.asn not in available_relays and \
                            scenario.probe_data_plane:
                        # TODO: Add Blackholes in LocalRIBs for this
                        outcomes[as_obj] = Outcomes.DISCONNECTED
            # Update Metadata tracking variables
            for relay_asn in scenario.relay_asns:
                before_relay_usage.update((outcomes[engine.as_dict[relay_asn]],))
                after_relay_usage.update((outcomes[engine.as_dict[relay_asn]],))
        # Update Metadata tracking variable
        after_relay_usage.update((self.available_relay_counter_key,) * len(available_relays))

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
                as_obj, scenario.ordered_prefix_subprefix_dict, attacker_ann.prefix, force_recompute=force_recompute)
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
                               attacker_ann_prefix: str,
                               force_recompute: bool = False
                               ) -> Optional[Ann]:
        """Returns the most specific announcement that exists in a rib

        as_obj is the as
        ordered prefixes are prefixes ordered from most specific to least
        """

        attacker_ann_prefix = ipaddress.ip_network(attacker_ann_prefix)
        for prefix in ordered_prefixes:
            if attacker_ann_prefix.subnet_of(ipaddress.ip_network(prefix)):
                most_specific_ann = as_obj._local_rib.get_ann(prefix)
                if most_specific_ann:
                    if not force_recompute:
                        # Mypy doesn't recognize that this is always an annoucnement
                        return most_specific_ann  # type: ignore
                    # Check if announcement traces back to a provider
                    provider_asns = tuple([x.asn for x in as_obj.providers])
                    if len(most_specific_ann.as_path) > 1 and most_specific_ann.as_path[1] in provider_asns:
                        # Mypy doesn't recognize that this is always an annoucnement
                        return most_specific_ann  # type: ignore
                    else:
                        # TODO: generate a test case for this block
                        return None
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
            if recompute_disconnections:
                if outcomes[as_obj] == Outcomes.DISCONNECTED and not isinstance(as_obj, scenario.AdoptASCls):
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
