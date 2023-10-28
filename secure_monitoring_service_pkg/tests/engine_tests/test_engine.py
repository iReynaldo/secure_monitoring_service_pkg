from pathlib import Path
import pytest
import random

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
from .engine_test_configs import Config135
from .engine_test_configs import Config136
from .engine_test_configs import Config137
from .engine_test_configs import Config138
from .engine_test_configs import Config139
from .engine_test_configs import Config140
from .engine_test_configs import Config141
from .engine_test_configs import Config142
from .engine_test_configs import Config143
from .engine_test_configs import Config144
from .engine_test_configs import Config145
from .engine_test_configs import Config146
from .engine_test_configs import Config147
from .engine_test_configs import Config148
from .engine_test_configs import Config149
from .engine_test_configs import Config150
from .engine_test_configs import Config151
from .engine_test_configs import Config152
from .engine_test_configs import Config153
from .engine_test_configs import Config154
from .engine_test_configs import Config155
from .engine_test_configs import Config156
from .engine_test_configs import Config157
from .engine_test_configs import Config158
from .engine_test_configs import Config159
from .engine_test_configs import Config160
from .engine_test_configs import Config161
from .engine_test_configs import Config162
from .engine_test_configs import Config163
from .engine_test_configs import Config164
from .engine_test_configs import Config165
from .engine_test_configs import Config166
from .engine_test_configs import Config167
from .engine_test_configs import Config168
from .engine_test_configs import Config169
from .engine_test_configs import Config170
from .engine_test_configs import Config171
from .engine_test_configs import Config172
# from .engine_test_configs import Config173
# from .engine_test_configs import Config174
# from .engine_test_configs import Config175

######################################
# Make tests deterministic
######################################

# IMPORTANT NOTE: PYTHONHASHSEED needs to be set in environment
# prior to running system tests!!!!!!!!!!!!
# Set random module's seed
random.seed(0)


######################################
# Test Engine
######################################

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
                              Config134,
                              Config135,
                              Config136,
                              Config137,
                              Config138,
                              Config139,
                              Config140,
                              Config141,
                              Config142,
                              Config143,
                              Config144,
                              Config145,
                              Config146,
                              Config147,
                              Config148,
                              Config149,
                              Config150,
                              Config151,
                              Config152,
                              Config153,
                              Config154,
                              Config155,
                              Config156,
                              Config157,
                              Config158,
                              Config159,
                              Config160,
                              Config161,
                              Config162,
                              Config163,
                              Config164,
                              Config165,
                              Config166,
                              Config167,
                              Config168,
                              Config169,
                              Config170,
                              Config171,
                              Config172,
                              # Config173,
                              # Config174,
                              # Config175,
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
