import random
from datetime import datetime
import csv

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine


caida_topology_date = "2023.04.29"
dl_time = datetime.strptime(caida_topology_date, "%Y.%m.%d")
dl_time.replace(hour=0, minute=0, second=0, microsecond=0)

print("Get AS Data")
engine = CaidaCollector(
    BaseASCls=BGPSimpleAS,
    GraphCls=SimulationEngine,
).run(dl_time=dl_time)

# Get degree and customer cone size
print("Calculating the ASN Degree and Customer Cone Size")
degree_dict = dict()
customer_cone_size_dict = dict()
for asn in engine.as_dict:
    as_obj = engine.as_dict[asn]
    degree_dict[asn] = len(as_obj.providers) + len(as_obj.customers) + len(as_obj.peers)
    customer_cone_size_dict[asn] = as_obj.customer_cone_size

# Compute rank
print("Calculating the AS RANK")
ranks_dict = dict()
ases_sorted_by_customer_conse_size = sorted(
    customer_cone_size_dict, key=customer_cone_size_dict.get, reverse=True
)
for asn in customer_cone_size_dict:
    ranks_dict[asn] = (
        ases_sorted_by_customer_conse_size.index(asn) + 1
    )  # largest customer cone size is 1 (not 0)

# Start CSV creation
with open("../../../data/graphs/metadata/asn_degree_and_rank.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    # Write header
    header = ["asn", "degree", "cone_size", "rank"]
    writer.writerow(header)
    # Collect all row information
    print("Creating CSV Rows Object")
    rows = list()
    for asn in degree_dict:
        rows.append(
            [asn, degree_dict[asn], customer_cone_size_dict[asn], ranks_dict[asn]]
        )
    # Write rows
    print("Writing CSV")
    writer.writerows(rows)
