#!/bin/bash
export PYTHONHASHSEED=0
python secure_monitoring_service_pkg/secure_monitoring_service_pkg/__main__.py --percentages 0.1 0.4 0.8 --num_trials 2 --policy v4 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 2 --scenario V4SubprefixHijackScenario
