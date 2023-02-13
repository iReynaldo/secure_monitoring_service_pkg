import random

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                        GraphCls=SimulationEngine,
                        ).run()
possible_ases = list(engine.stub_or_mh_asns)

previous_set = None
for k in [5, 10, 20, 100]:
    random.seed(0)
    print(f"Set of {k}")
    new_set = random.choices(possible_ases, k=k)
    if previous_set is None:
        previous_set = new_set
    print(f"Previous set is subset: {set(previous_set).issubset(set(new_set))}")
    print(new_set)
    previous_set = new_set

