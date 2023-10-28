#!/bin/bash
export PYTHONHASHSEED=0
python -m secure_monitoring_service_pkg --percentages 0.1 0.4 0.8 --num_trials 2 --policy v4 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
