from pathlib import Path
import pytest

from bgp_simulator_pkg import EngineTestConfig

from secure_monitoring_service_pkg.simulation_framework import sim_logger

from .utils.v4_engine_tester import V4EngineTester
from .engine_test_configs import Config100
from .engine_test_configs import Config101
from .engine_test_configs import Config102
from .engine_test_configs import Config103
from .engine_test_configs import Config104
from .engine_test_configs import Config105
from .engine_test_configs import Config106
from .engine_test_configs import Config107
from .engine_test_configs import Config108
from .engine_test_configs import Config109
from .engine_test_configs import Config110
from .engine_test_configs import Config111
from .engine_test_configs import Config112
from .engine_test_configs import Config113
from .engine_test_configs import Config114
from .engine_test_configs import Config115
from .engine_test_configs import Config116
from .engine_test_configs import Config117
from .engine_test_configs import Config118
from .engine_test_configs import Config119
from .engine_test_configs import Config120
from .engine_test_configs import Config121
from .engine_test_configs import Config122
from .engine_test_configs import Config123
from .engine_test_configs import Config124
from .engine_test_configs import Config125
from .engine_test_configs import Config126
from .engine_test_configs import Config127
from .engine_test_configs import Config128
from .engine_test_configs import Config129
from .engine_test_configs import Config130
from .engine_test_configs import Config131
from .engine_test_configs import Config132
from .engine_test_configs import Config133
from .engine_test_configs import Config134


@pytest.mark.engine
class TestEngine:
    """Performs a system test on the engine

    See README for in depth details
    """

    @pytest.mark.parametrize("conf",
                             [Config100,
                              Config101,
                              Config102,
                              Config103,
                              Config104,
                              Config105,
                              Config106,
                              Config107,
                              Config108,
                              Config109,
                              Config110,
                              Config111,
                              Config112,
                              Config113,
                              Config114,
                              Config115,
                              Config116,
                              Config117,
                              Config118,
                              Config119,
                              Config120,
                              Config121,
                              Config122,
                              Config123,
                              Config124,
                              Config125,
                              Config126,
                              Config127,
                              Config128,
                              Config129,
                              Config130,
                              Config131,
                              Config132,
                              Config133,
                              Config134
                              ])
    def test_engine(self, conf: EngineTestConfig, overwrite: bool):
        """Performs a system test on the engine

        See README for in depth details
        """
        sim_logger.CONDUCTING_SYSTEM_TEST = True

        V4EngineTester(base_dir=self.base_dir,
                       conf=conf,
                       overwrite=overwrite).test_engine()

    @property
    def base_dir(self) -> Path:
        """Returns test output dir"""

        return Path(__file__).parent / "engine_test_outputs"
