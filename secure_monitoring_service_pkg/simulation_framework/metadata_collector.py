import csv
import os

from filelock import FileLock

#########################################################
# Constants
#########################################################

CSV_FILE_DELIMITER = '\t'
HEADERS_WRITTEN = False

# Fieldnames
AVOID_LIST_CSV_FIELDNAMES = ['trial', 'percentage', 'propagation_round',
                             'adoption_setting', 'prefix_for_outcome',
                             'attacker_asns', 'victim_asn',
                             'relay_name', 'num_relays',
                             'edge_using_relay', 'etc_using_relay',
                             'input_clique_using_relay',
                             'before_relay_num_relays_hijacked',
                             'before_relay_num_relays_victim_success',
                             'before_relay_num_relays_disconnected',
                             'before_relay_num_relays_available',
                             'after_relay_num_relays_hijacked',
                             'after_relay_num_relays_victim_success',
                             'after_relay_num_relays_disconnected',
                             'after_relay_num_relays_available',
                             'avoid_list_len', 'avoid_list']

AS_CSV_FIELDNAMES = ['trial', 'percentage', 'propagation_round',
                     'adoption_setting', 'prefix_for_outcome',
                     'attacker_asns', 'victim_asn',
                     'relay_name', 'num_relays',
                     'asn', 'policy', 'num_providers',
                     'num_adopting_providers',
                     'outcome', 'using_adopting_provider',
                     'using_relay']

AGG_AS_CSV_FIELDNAMES = ['trial', 'percentage', 'propagation_round',
                         'adoption_setting', 'prefix_for_outcome',
                         'attacker_asns', 'victim_asn',
                         'relay_name']

# Add all the rest of the columns
#
# Abbreviation Meanings
# adoption_settings = {
#     'ad': 'adopting',
#     'nonad': 'non_adopting',
# }
# provider_setting = {
#     'noad': 'no adopting providers',
#     'al1ad': 'at least 1 adopting provider',
#     'allad': 'all adopting providers'
# }
#
for adoption_setting in ['ad', 'nonad']:
    for provider_setting in ['noad', 'al1ad', 'allad']:
        for using_adopting_provider_setting in ['using', 'notusing']:
            for topology_section in ['edge', 'etc', 'clique', 'all']:
                for outcome in ['hijacked', 'successful', 'disconnected']:
                    AGG_AS_CSV_FIELDNAMES.append(
                        '_'.join([adoption_setting, provider_setting,
                                  using_adopting_provider_setting, topology_section, outcome])
                    )

#########################################################
# Variables that need to be updated from __main__
#########################################################

output_filename = None
base_path = None

# Avoid List Metadata Collection
collect_avoid_list_metadata = False  # Defines control switch of enable/disabling metadata collection for avoid list
avoid_list_csv_filename = ''
avoid_list_csv_lock_filename = ''
avoid_list_csv_flock = None

# AS Metadata Collection
collect_as_metadata = False  # Defines control switch of enable/disabling metadata collection for each AS
as_csv_filename = ''
as_csv_lock_filename = ''
as_csv_flock = None

# Aggregate AS Metadata Collection
collect_agg_as_metadata = False  # Defines control switch of enable/disabling metadata collection for aggregated AS data
agg_as_csv_filename = ''
agg_as_csv_lock_filename = ''
agg_as_csv_flock = None


#########################################################
# Functions
#########################################################

def write_csv_file_header(csv_file_name, fieldnames, delimiter):
    # Write Header of CSV Files
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()


def write_avoid_list_csv_header():
    # Setup Metadata collection CSV
    global avoid_list_csv_filename
    global avoid_list_csv_lock_filename
    global avoid_list_csv_flock
    avoid_list_csv_filename = ''.join([base_path, '/', output_filename, '_avoid_list_metadata.csv'])
    avoid_list_csv_lock_filename = ''.join([avoid_list_csv_filename, '.lock'])
    avoid_list_csv_flock = FileLock(avoid_list_csv_lock_filename)
    # Write their headers
    write_csv_file_header(avoid_list_csv_filename, AVOID_LIST_CSV_FIELDNAMES, CSV_FILE_DELIMITER)


def write_as_csv_header():
    # Setup Metadata collection CSV
    global as_csv_filename
    global as_csv_lock_filename
    global as_csv_flock
    as_csv_filename = ''.join([base_path, '/', output_filename, '_as_metadata.csv'])
    as_csv_lock_filename = ''.join([as_csv_filename, '.lock'])
    as_csv_flock = FileLock(as_csv_lock_filename)
    # Write their headers
    write_csv_file_header(as_csv_filename, AS_CSV_FIELDNAMES, CSV_FILE_DELIMITER)


def write_agg_as_csv_header():
    # Setup Metadata collection CSV
    global agg_as_csv_filename
    global agg_as_csv_lock_filename
    global agg_as_csv_flock
    agg_as_csv_filename = ''.join([base_path, '/', output_filename, '_agg_as_metadata.csv'])
    agg_as_csv_lock_filename = ''.join([agg_as_csv_filename, '.lock'])
    agg_as_csv_flock = FileLock(agg_as_csv_lock_filename)
    # Write their headers
    write_csv_file_header(agg_as_csv_filename, AGG_AS_CSV_FIELDNAMES, CSV_FILE_DELIMITER)


def clean_up_lock_files():
    if collect_avoid_list_metadata:
        os.remove(avoid_list_csv_lock_filename)
    if collect_as_metadata:
        os.remove(as_csv_lock_filename)
    if collect_agg_as_metadata:
        os.remove(agg_as_csv_lock_filename)
