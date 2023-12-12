#!/bin/bash

python convert_rov_json_to_csv.py data/rov_info.json
grep -E 'Friends,[2-7]|ROVISTA|APNIC' data/rov_info.csv > data/rov_info_friends_apnic_rovista.csv
sed -i 1s/^/"asn,filtering,confidence,source,category\n"/g data/rov_info_friends_apnic_rovista.csv
cp data/rov_info_friends_apnic_rovista.csv ../secure_monitoring_service_pkg/aux_files/rov_adoption_real.csv

