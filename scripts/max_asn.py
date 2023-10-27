import heapq

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


print("Loading Caida Data")
engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
).run()

print("Calculating Answer")
print(heapq.nlargest(1, engine.as_dict.keys()))
