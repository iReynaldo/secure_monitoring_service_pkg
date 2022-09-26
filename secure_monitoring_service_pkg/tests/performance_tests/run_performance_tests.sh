#!/bin/sh

# IMPORTANT NOTE:
# Make sure the python environment is activated before this script is run

export PYTHONHASHSEED="1"

for policy in v1 v4 v4k1
do
    for percent in 1 10 40 80
    do
        for num_trials in 10 20 30 60
        do
            echo "Running ${policy} at ${percent}% adoption for ${num_trials} trials"
            # time pypy -m cProfile -o "performance_${policy}_${percent}_percent_${num_trials}_trial.profile" performance_tester.py $policy $percent $num_trials
            formatted_string=$(echo '{\n"policy":' ${policy} ',\n"percentage":' ${percent} ',\n"trials":' $num_trials ',\n"avg_unshared_memory": %D,\n"avg_memory": %K,\n"avg_set_memory": %t,\n"max_memory": %M,\n"total_time": %e,\n"cpu": "%P"\n}')
            time -f "${formatted_string}" pypy performance_tester.py ${policy} ${percent} ${num_trials}
        done
    done
done
