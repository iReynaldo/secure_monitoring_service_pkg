#!/bin/bash

# IMPORTANT NOTE:
# Make sure the python environment is activated before this script is run


####################################
# Environment Variables
####################################

export PYTHONHASHSEED=0;


####################################
# Input Arguments
####################################

# Check number of args is satisfied
if [[ "$#" != "2" || ( $@ == "--help" ) ||  $@ == "-h"  ]]; then
    echo "USAGE: ${0} [scenario] [tag] | [-h | --help]"
    echo "scenario: V4SubprefixHijackScenario | SubprefixAutoImmuneScenario"
    exit 1
fi

# Set Input Argument Variables
scenario=${1}
tag=${2}  # Optional Argument


####################################
# Main Loop
####################################


for policy in v1 v4 v4k1 v4k5
do
    for percent in 0.01 0.1 0.4 0.8
    do
        for num_trials in 10 20 30 60 100
        do
            echo "Running ${policy} at ${percent}% adoption for ${num_trials} trials"
            python probe.py --scenario ${scenario} --policy ${policy} --percentages ${percent} --num_trials ${num_trials} --cpus 12 --tag ${tag}
        done
    done
done

