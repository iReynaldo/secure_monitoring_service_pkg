from collections import defaultdict
import copy
import ipaddress
from typing import Dict, Set, List, Tuple
from collections import defaultdict

from bgp_simulator_pkg import Announcement as Ann

from secure_monitoring_service_pkg.simulation_engine import mvdp
from secure_monitoring_service_pkg.simulation_framework.sim_logger import sim_logger as logger


class TrustedServer:
    __slots__ = ("_raw_data",
                 "_recommendations",
                 "_make_recs",
                 "_max_num_dishonest_nodes",
                 "scenario_name",
                 "prefix_provider_mapping",
                 "adopters_with_blackhole")
    name = "TrustedServer"

    def __init__(self, max_num_dishonest_nodes: int = 0):
        # {prefix: ann_Set}
        self._max_num_dishonest_nodes: int = max_num_dishonest_nodes
        self._raw_data: Dict[str, List[Ann]] = \
            defaultdict(list)
        self._recommendations: Dict[str, Set[int]] = defaultdict(set)
        self._make_recs = False
        # The following two get initiated after propagation in
        # V4Scenatio apply_blackholes_from_avoid_list
        self.scenario_name = None
        self.prefix_provider_mapping = None  # Only in SubprefixAutoImmuneScenario
        self.adopters_with_blackhole: Dict[str, Set[int]] = defaultdict(set)  # per prefix, ASNs in the sets are adopters that have blackholes

    def rec_blackhole(self, subprefix: str, as_path: Tuple[int, ...]) -> bool:
        """Recommends a blackhole for a subprefix"""

        # Checks if the suspect is in the given as_path
        for suspect in self._recommendations.get(subprefix, []):
            if suspect in as_path:
                return True
        return False

    def receive_report(self, unprocessed_invalid_ann):
        """Process report about an invalid ann"""

        self._raw_data[unprocessed_invalid_ann.prefix].append(
            unprocessed_invalid_ann)

    def create_recs(self):
        logger.debug("Inside create_recs")
        previous_prefix = None
        for prefix in self._raw_data:
            if not (self.scenario_name == "SubprefixAutoImmuneScenario" and previous_prefix):
                self.update_recs(prefix)
            else:
                self.update_recs(prefix, False, previous_prefix)
            logger.debug(f"Path List for {prefix}: {self.reports_to_path_list(prefix)}")
            logger.debug(f"Avoid List for {prefix}:  {self._recommendations[prefix]}")
            previous_prefix = prefix

    def update_recs(self, prefix, recompute=True, previous_prefix=None):
        """Updates recommendations"""

        if self._max_num_dishonest_nodes == 0:
            for ann in self._raw_data[prefix]:
                self._recommendations[ann.prefix].update(ann.as_path)
        elif self._max_num_dishonest_nodes > 0:
            if recompute:
                self._recommendations[prefix] = mvdp.get_avoid_list(self.reports_to_path_list(prefix), self._max_num_dishonest_nodes)
            else:
                assert previous_prefix, "Cannot copy avoid list on None value for previous_prefix"
                # Base answer on existing recommendations
                previous_target_asn = self.prefix_provider_mapping[previous_prefix]
                target_asn = self.prefix_provider_mapping[prefix]

                self._recommendations[prefix] = copy.copy(self._recommendations[previous_prefix])
                if previous_target_asn in self._recommendations[prefix]:
                    self._recommendations[prefix].remove(previous_target_asn)

                self._recommendations[prefix].extend(
                    mvdp.get_avoid_list(
                        self.reports_to_path_list(prefix),
                        self._max_num_dishonest_nodes,
                        {target_asn,}
                    )
                )

    def reports_to_path_list(self, prefix):
        """
        For a given prefix, return the edge list
        for the associated list of reports.
        """
        path_list = list()  # Will be a list of tuples (i.e. edge list)
        for ann in self._raw_data[prefix]:
            path_list.append(ann.as_path)
        return path_list

    def has_blackhole(self, asn, attacker_prefix, engine) -> bool:
        as_obj = engine.as_dict[asn]
        attacker_ann_from_relay_local_rib = as_obj._local_rib.get_ann(attacker_prefix)
        if attacker_ann_from_relay_local_rib and attacker_ann_from_relay_local_rib.blackhole:
            return True
        return False

    def gather_blackhole_information(self, attacker_prefix, engine):
        for avoid_list_set in self._recommendations.values():
            for asn in avoid_list_set:
                if self.has_blackhole(asn, attacker_prefix, engine):
                    self.adopters_with_blackhole[attacker_prefix].add(asn)

    def reset(self):
        del self._raw_data
        self._raw_data: Dict[str, List[Ann]] = \
            defaultdict(list)
        del self._recommendations
        self._recommendations: Dict[str, Set[int]] = defaultdict(set)
