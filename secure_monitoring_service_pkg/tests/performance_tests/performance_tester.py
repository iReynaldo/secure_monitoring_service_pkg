from bgp_simulator_pkg import Simulator, BGPAS, Graph
from secure_monitoring_service_pkg.simulation_framework.scenarios.v4_subprefix_hijack_scenario import V4SubprefixHijack
from secure_monitoring_service_pkg.rov_sms import ROVSMS, ROVSMSK1
from lib_rovpp import ROVPPV1SimpleAS

import random
import sys

random.seed(1)

# Read in arguments
policy_str=sys.argv[1]
perentage=int(sys.argv[2])
num_trials=int(sys.argv[3])

# Interpret the policy_str
if policy_str == "v1":
    policy = ROVPPV1SimpleAS
elif policy_str == "v4":
    policy = ROVSMS
elif policy_str == "v4k1":
    policy = ROVSMSK1
else:
    assert(False, "Unrecognized policy specified. Use following options {v1, v4, v4k1}")


if __name__ == "__main__":
    Simulator().run(graphs=[Graph(percent_adoptions=[perentage],
                                  adopt_as_classes=[policy],
                                  EngineInputCls=V4SubprefixHijack,
                                  num_trials=num_trials,
                                  BaseASCls=BGPAS)]
                    )

