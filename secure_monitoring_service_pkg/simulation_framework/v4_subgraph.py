from typing import Dict, Any, Type, Tuple

from caida_collector_pkg import AS

from bgp_simulator_pkg import SimulationEngine
from bgp_simulator_pkg import Scenario
from bgp_simulator_pkg import Subgraph
from bgp_simulator_pkg import Outcomes

from rovpp_pkg import ROVPPV1SimpleAS
from rovpp_pkg import ROVPPV1LiteSimpleAS

# TODO: Re-introduce metadata_collector
# from secure_monitoring_service_pkg.simulation_framework import metadata_collector


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

    # TODO: Move this percentage and trial capturing somewhere
    # metadata_collector.cur_percent_adoption = percent_adopt
    # metadata_collector.cur_trial = trial


    # MARK: Needs to be fixed
    # TODO: Update this to support multiple attackers and victims
    def verify_avoid_list(self, engine, scenario, outcomes, traceback_asn_outcomes):
        """
        Makes sure that all the members of the avoid list 'don't lead to victim'
        (This satisfies the check that all members of the avoid list 'lead to
        the attacker'; which may not necessariy always happen if disconnecitions
        are created due to V4 or other reasons).
        :param engine:
        :param scenario:
        :param traceback_asn_outcomes:
        :param outcomes:
        :return:
        """

        # Check that the avoid list ASes always lead to attacker
        # print(outcomes)
        for prefix in scenario.avoid_lists:
            for asn in scenario.avoid_lists[prefix]:
                # TODO: Figure out why using the enum doesn't work
                # TODO: For some reason it literally prints "ASNs.Attacker"
                # print(f"Attacker: {enums.ASNs.ATTACKER}")
                # print(f"Victim: {enums.ASNs.VICTIM}")
                # TODO: The following commented out conditional doesn't work because above TODO
                # if asn != enums.ASNs.ATTACKER and asn != enums.ASNs.VICTIM:
                if asn != 666 and asn != 777:
                    # print(asn)  # TODO: you can also see that 666 slips through
                    if asn in outcomes:
                        assert outcomes[asn] != Outcomes.VICTIM_SUCCESS, \
                            f"ASN: {asn} in avoid list leads to victim"
                        # Check if the disconnected case is not caused by a blackhole
                        as_obj = engine.as_dict[traceback_asn_outcomes[asn]]
                        # TODO: the following check wouldn't work for v2, v2a, and v3
                        if outcomes[asn] == Outcomes.DISCONNECTED \
                                and not (isinstance(as_obj, ROVPPV1SimpleAS)
                                         or isinstance(as_obj, ROVPPV1LiteSimpleAS)):
                            assert f"ASN: {asn} in avoid list was disconnected, but not by a blackhole."

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

        if not shared_data.get("set"):
            # {as_obj: outcome}
            outcomes, traceback_asn_outcomes = \
                self._get_engine_outcomes(engine, scenario)
            if scenario.has_rovsms_ases:
                self.verify_avoid_list(engine, scenario, outcomes, traceback_asn_outcomes)
            self._add_traceback_to_shared_data(shared_data,
                                               engine,
                                               scenario,
                                               outcomes)
        key = self._get_subgraph_key(scenario)
        self.data[propagation_round][scenario.graph_label][percent_adopt
            ].append(shared_data.get(key, 0))  # noqa

    # MARK: New
    def _get_as_outcome(self,
                        as_obj: AS,
                        outcomes: Dict[AS, Outcomes],
                        traceback_asn_outcomes: Dict[int, int],
                        engine: SimulationEngine,
                        scenario: Scenario
                        ) -> Tuple[Type[Outcomes], Type[int]]:
        """Recursively returns the as outcome"""

        if as_obj in outcomes:
            return outcomes[as_obj], traceback_asn_outcomes[as_obj.asn]
        else:
            # Get the most specific announcement in the rib
            most_specific_ann = self._get_most_specific_ann(
                as_obj, scenario.ordered_prefix_subprefix_dict)
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
                                                              scenario)
            assert outcome != Outcomes.UNDETERMINED, "Shouldn't be possible"

            outcomes[as_obj] = outcome
            traceback_asn_outcomes[as_obj.asn] = traceback_asn
            return outcome, traceback_asn

    # MARK: New
    def _get_engine_outcomes(self,
                             engine: SimulationEngine,
                             scenario: Scenario
                             ) -> Tuple[Dict[AS, Outcomes], Dict[int, int]]:
        """Gets the outcomes of all ASes"""

        # {ASN: outcome}
        outcomes: Dict[AS, Outcomes] = dict()
        traceback_asn_outcomes: Dict[int, int] = dict()
        for as_obj in engine.as_dict.values():
            # Gets AS outcome and stores it in the outcomes dict
            self._get_as_outcome(as_obj,
                                 outcomes,
                                 traceback_asn_outcomes,
                                 engine,
                                 scenario)
        return outcomes, traceback_asn_outcomes
