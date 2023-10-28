#!/bin/bash
export PYTHONHASHSEED=0


# About 52s with cprofile
# write tsv is taking 15s..... why is this getting called ever???
# boom - 10 seconds erased with that. Down to 42s
# Removed subnet_of ops, down to 39.5s
# Removed more subnet calls, down to 36s
# Rewrote rec_blackholes, down to 34s.
# Considering that graphing takes >10s, and CaidaCollector initial build > 10s,
# that means rest of program was only 32s to begin with, and now is 14s.
# That's somewhere between a 2-3x speedup since those fixed costs are near zero when running many trials
time pypy3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 2 --policy v4 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
# time python3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 2 --policy v4 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario


# again, two minutes each
#time pypy3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 20 --policy v4 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
#time python3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 20 --policy v4 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario

# Below, runtime is identical, 58s on Justin's lenovo
#time pypy3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 20 --policy v4 --cpus 10 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
#time python3 -O -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 20 --policy v4 --cpus 10 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
