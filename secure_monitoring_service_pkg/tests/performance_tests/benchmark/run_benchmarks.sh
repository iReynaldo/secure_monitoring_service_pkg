#!/bin/sh

# IMPORTANT NOTE:
# Make sure the python environment is activated before this script is run

tag=${1}

for policy in v1 v4 v4k1 v4k5
do
    for percent in 0.01 0.1 0.4 0.8
    do
        for num_trials in 10 20 30 60 100
        do
            echo "Running ${policy} at ${percent}% adoption for ${num_trials} trials"
            pypy probe.py --policy ${policy} --percentages ${percent} --num_trials ${num_trials} --cpus 12 --tag ${tag}
        done
    done
done

