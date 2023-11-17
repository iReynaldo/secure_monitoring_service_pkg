# Import config variables
from .config_100 import config_100
from .config_104 import config_104

# Specify module imports
__all__ = [
    "config_100",
    "config_104"
]

# Config variable holder
engine_test_configs = [
    config_100,
    config_104,
]