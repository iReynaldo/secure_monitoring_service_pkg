from collections import defaultdict
from typing import Dict, Set, List, Tuple

from lib_bgp_simulator import Announcement as Ann

from lib_secure_monitoring_service import mvdp


class TrustedServer:
    __slots__ = ("_raw_data", "_recommendations", "_make_recs", "_max_num_dishonest_nodes")
    name = "TrustedServer"

    def __init__(self, max_num_dishonest_nodes=0):
        # {prefix: ann_Set}
        self._max_num_dishonest_nodes: Int = max_num_dishonest_nodes
        self._raw_data: Dict[str, List[Ann]] = \
            defaultdict(list)
        self._recommendations: Dict[str, Set[int]] = defaultdict(set)
        self._make_recs = False

    def rec_blackhole(self, subprefix: str, as_path: Tuple[int, ...]) -> bool:
        """Recommends a blackhole for a subprefix"""

        # Checks if the suspect is in the given as_path
        for suspect in self._recommendations.get(subprefix, []):
            if suspect in as_path:
                return True
        return False

    def recieve_report(self, unprocessed_invalid_ann):
        """Process report about an invalid ann"""

        assert unprocessed_invalid_ann.invalid_by_roa

        self._raw_data[unprocessed_invalid_ann.prefix].append(
            unprocessed_invalid_ann)

        # TODO: try moving this to post propagation hook
        self.update_recs(unprocessed_invalid_ann.prefix)

    def update_recs(self, prefix):
        """Updates recommendations"""

        if self._max_num_dishonest_nodes == 0:
            for ann in self._raw_data[prefix]:
                self._recommendations[ann.prefix].update(ann.as_path)
        elif self._max_num_dishonest_nodes > 0:
            self._recommendations[prefix] = mvdp.get_avoid_list(self.reports_to_path_list(prefix), self._max_num_dishonest_nodes)

    def reports_to_path_list(self, prefix):
        """
        For a given prefix, return the edge list
        for the associated list of reports.
        """
        path_list = list()  # Will be a list of tuples (i.e. edge list)
        for ann in self._raw_data[prefix]:
            path_list.append(ann.as_path)
        return path_list
