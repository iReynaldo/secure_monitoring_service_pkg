import csv
import os

from lib_bgp_simulator.simulator.scenario import Scenario
from lib_bgp_simulator.enums import Relationships

from lib_secure_monitoring_service.rov_sms import ROVSMS
from lib_secure_monitoring_service.sim_logger import sim_logger as logger
from lib_secure_monitoring_service import metadata_collector

class V4Scenario(Scenario):

    trusted_server_ref = None

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
        with open('as_metadata.tsv', 'a') as csvfile: # TODO: Remove this context once done collecting AS metadata
            # TODO: Delete the following lines once reports collected
            # -------------------------------------------------------------
            fieldnames = [
                'percentAdoption', 'trial', 'asn', 'adopting', 'legitPrefixASPath', 'rank',
                'numPeers', 'numProviders', 'numCustomers', 'degree', 'subgraph'
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
                            reports_path_list= list()
                            num_reports=0
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
                    numProviders =len(as_obj.providers)
                    numCustomers = len(as_obj.customers)
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
                        'subgraph': subg_name
                    }
                    writer.writerow(row)
                    # -------------------------------------------------------------



    def run(self, subgraphs, propagation_round: int):
        # Run engine
        self.engine.run(propagation_round=propagation_round,
                        engine_input=self.engine_input)
        # Add blackholes from avoid list
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
        # Emtpy the trusted server
        if self.trusted_server_ref:
            self.trusted_server_ref.reset()
            # Note the trusted_server_ref is set inside apply_blackholes_from_avoid_list
            self.trusted_server_ref = None

        return traceback_outcomes