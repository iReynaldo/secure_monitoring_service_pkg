#!/bin/sh

# IMPORTANT NOTE:
# Make sure the python environment is activated before this script is run

export PYTHONHASHSEED="1"

for policy in v1 v4 v4k1
do
    for percent in 1
    do
        for num_trials in 10
        do
            echo "Running ${policy} at ${percent}% adoption for ${num_trials} trials"
            time python -m cProfile -o "performance_${policy}_${percent}_percent_${num_trials}_trial.profile" performance_tester.py $policy $percent $num_trials
        done
    done
done
