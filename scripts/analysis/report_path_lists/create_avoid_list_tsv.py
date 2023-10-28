import time
from datetime import datetime
import importlib
import csv
import os
import sys

from secure_monitoring_service_pkg import mvdp

# Collect input args
try:
    assert len(sys.argv) == 2, "Just specify number of modules as argument"
    num_modules = int(sys.argv[1])
except ValueError:
    print("Argument must be an integer")

# Track when this was computed
timestamp = datetime.now().isoformat()
tsv_start_time = time.perf_counter()
print("Start Time: ", timestamp)

# Create TSV within this file
with open("avoid_list.tsv", "w") as csvfile:
    fieldnames = [
        "percentAdoption",
        "k",
        "trial",
        "computeTime",
        "attackerASN",
        "victimASN",
        "numAdopting",
        "numReports",
        "attackerInAvoidList",
        "attackerProviders",
        "attackerProviderInAvoidList",
        "avoidListSize",
        "avoidList",
        "adoptingASNs",
        "machineName",
        "timestamp",
    ]
    writer = csv.DictWriter(csvfile, delimiter="\t", fieldnames=fieldnames)
    writer.writeheader()
    for i in range(num_modules):
        # Get the module (e.g. x001, x002, ... x010)
        module_name = "x{0:{fill}{align}3}".format(i, fill="0", align=">")
        path_list_module = importlib.import_module(module_name)
        for k in [1, 2, 3, 4, 5, 7, 10]:
            # Collect the items write to csv
            start_time = time.perf_counter()
            avoid_list = mvdp.get_avoid_list(path_list_module.reports_path_list, k)
            compute_time = time.perf_counter() - start_time
            avoid_list_size = len(avoid_list)
            attackerInAvoidList = path_list_module.attacker_asn in avoid_list
            attackerProviderInAvoidList = any(
                x in path_list_module.attacker_providers for x in avoid_list
            )
            num_adopting = len(path_list_module.adopting_asns)
            # Create row to write to tsv
            row = {
                "percentAdoption": path_list_module.percent_adoption,
                "k": k,
                "trial": path_list_module.trial,
                "computeTime": compute_time,
                "attackerASN": path_list_module.attacker_asn,
                "victimASN": path_list_module.victim_asn,
                "numAdopting": num_adopting,
                "numReports": path_list_module.num_reports,
                "attackerInAvoidList": attackerInAvoidList,
                "attackerProviders": path_list_module.attacker_providers,
                "attackerProviderInAvoidList": attackerProviderInAvoidList,
                "avoidListSize": avoid_list_size,
                "avoidList": avoid_list,
                "adoptingASNs": path_list_module.adopting_asns,
                "machineName": os.uname().nodename,
                "timestamp": timestamp,
            }
            # Write to tsv
            writer.writerow(row)

print("End Time: ", datetime.now().isoformat())
print("Elapsed Time: ", time.perf_counter() - tsv_start_time)
