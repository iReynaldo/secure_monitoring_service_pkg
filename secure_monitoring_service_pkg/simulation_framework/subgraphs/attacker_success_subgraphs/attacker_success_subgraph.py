from abc import abstractmethod
from typing import TYPE_CHECKING

from secure_monitoring_service_pkg import V4Subgraph


if TYPE_CHECKING:
    from bgp_simulator_pkg import Scenario


class AttackerSuccessSubgraph(V4Subgraph):
    """A subgraph for data display"""

    @abstractmethod
    def _get_subgraph_key(self, scenario: "Scenario", *args) -> str:
        """Returns the key to be used in shared_data on the subgraph"""

        raise NotImplementedError

    @property
    @abstractmethod
    def y_axis_label(self) -> str:
        """returns y axis label"""

        raise NotImplementedError
