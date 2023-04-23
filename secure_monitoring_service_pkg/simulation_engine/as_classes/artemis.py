import random

from bgp_simulator_pkg import BGPSimpleAS

from secure_monitoring_service_pkg.simulation_framework.sim_logger import sim_logger as logger
from secure_monitoring_service_pkg.simulation_engine.report import Report


class Artermis(BGPSimpleAS):
    name = "ARTEMIS"

    def __init__(self, *args, **kwargs):
        """ARTEMIS Mitigation Policy"""
        super(Artermis, self).__init__(*args, **kwargs)
