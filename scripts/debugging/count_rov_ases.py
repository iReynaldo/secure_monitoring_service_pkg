import random
from pathlib import Path

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


print("Loading CAIDA Topology")
engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
    GraphCls_kwargs={
        "csv_path": Path(
            "../secure_monitoring_service_pkg/aux_files/rov_adoption_5.csv"
        )
    },
).run()

print("Counting ASes")
count = 0
for as_obj in engine.ases:
    if as_obj.rov_confidence >= 0:
        count += 1
print(count)
