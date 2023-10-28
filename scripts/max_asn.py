import heapq

from bgpy import CaidaCollector

from bgpy import BGPSimpleAS
from bgpy import SimulationEngine


print("Loading Caida Data")
engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
).run()

print("Calculating Answer")
print(heapq.nlargest(1, engine.as_dict.keys()))
