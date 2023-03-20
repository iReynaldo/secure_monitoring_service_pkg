"""
CSV creation taken from
https://www.geeksforgeeks.org/writing-csv-files-in-python/
"""
import csv
import shutil
import random
import copy

from caida_collector_pkg import CaidaCollector

from bgp_simulator_pkg import BGPSimpleAS
from bgp_simulator_pkg import SimulationEngine

#########################
# Constants
#########################

# Path to real rov adoption
path_to_real_rov_adoption = '../secure_monitoring_service_pkg/aux_files/rov_adoption_real.csv'
base_path_to_new_path = '../secure_monitoring_service_pkg/aux_files'

# field names
# fields = ['asn', 'filtering', 'confidence', 'source']

#########################
# Main
#########################

print("Loading CAIDA information")
# Get possible ASes
engine = CaidaCollector(BaseASCls=BGPSimpleAS,
                        GraphCls=SimulationEngine,
                        ).run()
all_ases_set = engine.stub_or_mh_asns
possible_ases_set = copy.deepcopy(all_ases_set)
print("Done loading CAIDA information")

# load default ROV ASes
default_rov_ases = list()
with open(path_to_real_rov_adoption, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        asn = int(row['asn'])
        default_rov_ases.append(asn)
        possible_ases_set.discard(asn)

# List of possible ASes to select from
possible_ases_list = list(possible_ases_set)

# Precalculated numbers
num_all_ases = len(all_ases_set)
num_default_rov_ases = len(default_rov_ases)

# Create a file for different ROV percent adoptions
for perc in [5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90]:
    print(f"Creating file for ROV setting {perc}%")
    # name of output csv file
    filename = f"rov_adoption_{perc}.csv"
    new_output_file_path = '/'.join([base_path_to_new_path, filename])

    # Copy from original real rov adoption
    shutil.copyfile(path_to_real_rov_adoption, new_output_file_path)

    # Calculate additional ASes needed
    total_num_ases_needed = int(0.01 * perc * num_all_ases)
    remaining_num_ases_needed = total_num_ases_needed - num_default_rov_ases

    rows = list()
    # writing to csv file
    with open(new_output_file_path, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # Uniformly random select additional ROV ASes
        random.seed(0)
        asn_list = random.choices(possible_ases_list, k=remaining_num_ases_needed)
        # Create row records
        for asn in asn_list:
            rows.append([str(asn), 'all', '1', 'synthetic'])
        # Write the data rows
        csvwriter.writerows(rows)
