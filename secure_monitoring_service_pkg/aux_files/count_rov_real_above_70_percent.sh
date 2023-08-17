#!/bin/bash

awk -F, 'NR>1 { if ($3>0.7) {print $3} }' rov_adoption_real.csv | wc -l
