import random
from datetime import datetime

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


caida_topology_date = "2023.04.29"
dl_time = datetime.strptime(caida_topology_date, "%Y.%m.%d")
dl_time.replace(hour=0, minute=0, second=0, microsecond=0)

engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
).run(dl_time=dl_time)
possible_ases = list(engine.stub_or_mh_asns)

previous_set = None
for k in [5, 10, 20, 40, 50, 100]:
    random.seed(0)
    print(f"Set of {k}")
    new_set = random.choices(possible_ases, k=k)
    if previous_set is None:
        previous_set = new_set
    print(f"Previous set is subset: {set(previous_set).issubset(set(new_set))}")
    print(new_set)
    previous_set = new_set
