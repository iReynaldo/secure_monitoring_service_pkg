import random
from datetime import datetime
from pathlib import Path

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


HOME_DIR = str(Path.home())
CAIDA_CACHE_DIR = HOME_DIR + "/tmp/caida_collector_cache"
CAIDA_CACHE_TSV = HOME_DIR + "/tmp/caida_collector.tsv"

caida_topology_date = "2023.05.07"  # '2023.04.29'
dl_time = datetime.strptime(caida_topology_date, "%Y.%m.%d")
dl_time.replace(hour=0, minute=0, second=0, microsecond=0)

engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
).run(dl_time=dl_time, cache_dir=Path(CAIDA_CACHE_DIR), tsv_path=Path(CAIDA_CACHE_TSV))

print(f"Number of ASes in topology: {len(engine.ases)}")
print(f"Number of Stubs or Multihomed ASes: {len(engine.stub_or_mh_asns)}")
print(f"Number of Etc ASes: {len(engine.etc_ases)}")
print(f"Number of in Input Clique: {len(engine.input_clique_ases)}")
