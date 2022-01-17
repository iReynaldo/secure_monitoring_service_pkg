from collections import defaultdict
from typing import Dict, List, Tuple

from lib_bgp_simulator import Announcement as Ann

from .report import Report


class TrustedServer:
    __slots__ = ("raw_data", "recommendations")

    def __init__(self):
        # {prefix: ann_list}
        self._raw_data: Dict[str, List[Ann]] =\
            defaultdict(list)
        self._recommendations: Dict[str, List[int]] = defaultdict(list)

    def rec_blackhole(subprefix: str, as_path: Tuple[int, ...]) -> bool:
        """Recommends a blackhole for a subprefix"""

        
        raise NotImplementedError

    def recieve_report(self, unprocessed_invalid_ann):
        """Process report about an invalid ann"""

        assert unprocessed_invalid_ann.invalid_by_roa

        self._raw_data[unprocessed_invalid_ann.prefix].append(
            unprocessed_invalid_ann)

        self.updated_recs(unprocessed_invalid_ann.prefix)

    def update_recs(self, prefix):
        """Updates recommendations"""

        anns = self._raw_data[prefix]
        
