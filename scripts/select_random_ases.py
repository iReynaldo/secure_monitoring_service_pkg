import random

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine

random.seed(0)

engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                        GraphCls=SimulationEngine,
                        ).run()
possible_ases = list(engine.stub_or_mh_asns)

print("Set of 20")
print(random.choices(possible_ases, k=20))

print("Set of 100")
print(random.choices(possible_ases, k=100))

print("Set of 5")
print(random.choices(possible_ases, k=5))

print("Set of 10")
print(random.choices(possible_ases, k=10))
