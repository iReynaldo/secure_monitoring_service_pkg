#!/bin/bash

awk -F, 'NR>1 { if ($3>0.1) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.2) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.3) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.4) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.5) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.6) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.7) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.8) {print $3} }' rov_adoption_real.csv | wc -l
awk -F, 'NR>1 { if ($3>0.9) {print $3} }' rov_adoption_real.csv | wc -l
