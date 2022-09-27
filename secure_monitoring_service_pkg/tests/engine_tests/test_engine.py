from pathlib import Path
import pytest

from bgp_simulator_pkg import EngineTestConfig

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
                              Config112])
    def test_engine(self, conf: EngineTestConfig, overwrite: bool):
        """Performs a system test on the engine

        See README for in depth details
        """

        V4EngineTester(base_dir=self.base_dir,
                       conf=conf,
                       overwrite=overwrite).test_engine()

    @property
    def base_dir(self) -> Path:
        """Returns test output dir"""

        return Path(__file__).parent / "engine_test_outputs"
