from pathlib import Path
import pytest

from bgp_simulator_pkg import EngineTestConfig

from .utils.v4_engine_tester import V4EngineTester
from .engine_test_configs import Config100


@pytest.mark.engine
class TestEngine:
    """Performs a system test on the engine

    See README for in depth details
    """

    @pytest.mark.parametrize("conf",
                             [Config100,
                              ])
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
