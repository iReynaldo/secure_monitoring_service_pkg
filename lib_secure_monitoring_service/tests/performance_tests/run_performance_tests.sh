#!/bin/sh

# IMPORTANT NOTE:
# Make sure the python environment is activated before this script is run

output_file_template="performance_${policy}_${percent}_percent_${num_trials}_trial.profile"

for policy in v1 v4 v4k1
do
    for percent in 80
    do
        for num_trials in 10
        do
            echo "Running ${policy} at ${percent}% adoption for ${num_trials} trials"
            python -m cProfile -o "performance_${policy}_${percent}_percent_${num_trials}_trial.profile" performance_tester.py $policy $percent $num_trials
        done
    done
done
