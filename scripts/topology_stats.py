from datetime import datetime

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


dl_time = datetime.strptime('2023.05.07', '%Y.%m.%d')
dl_time.replace(hour=0, minute=0, second=0, microsecond=0)
engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                        GraphCls=SimulationEngine,
                        ).run(dl_time=dl_time)

print(f"Fraction of edge ASes that are multihomed: {len(engine.mh_asns)/len(engine.stub_or_mh_asns)}")

asn = 48528
print(f"Analyzing the providers of {asn}")
print(f"The providers are: {[as_obj.asn for as_obj in engine.as_dict[asn].providers]}")
