from collections import defaultdict
from typing import Dict, Set, List, Tuple

from lib_bgp_simulator import Announcement as Ann


class TrustedServer:

    __slots__ = ("_raw_data", "_recommendations", "_make_recs")
    name="TrustedServer"

    def __init__(self):
        # {prefix: ann_Set}
        self._raw_data: Dict[str, List[Ann]] =\
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

        self.update_recs(unprocessed_invalid_ann.prefix)

    def update_recs(self, prefix):
        """Updates recommendations"""

        for ann in self._raw_data[prefix]:
            self._recommendations[ann.prefix].update(ann.as_path)
