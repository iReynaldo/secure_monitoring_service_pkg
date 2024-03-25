#!/bin/bash

#for relay in neustar verisign cloudflare incapsula
#do
#for scenario in V4OriginHijack
#for scenario in RelayPrefixHijack
#for scenario in RelayPrefixHijack V4SubprefixHijackScenario V4PrefixHijackScenario
for scenario in V4SubprefixHijackScenario V4PrefixHijackScenario
do
#for attacker in 5
#for attacker in 1 5 10 20
for attacker in 10 20
do
for thresh in 0 10 20 30 40 50 60 70 80 90 100
do
    #python convert_json_to_csv.py "./jsons/RelayPrefixHijack_scenario_none_type_standard_policies_real_rov_${thresh}_conf_False_turnover_0_hash_False_probe_False_tunnel_${relay}_relay_False_attackRelay_1_attacker_2000_trials_[0.0,0.01]_percentages.json"
    python convert_json_to_csv.py "./jsons/${scenario}_scenario_none_type_standard_policies_real_rov_${thresh}_conf_False_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_${attacker}_attacker_2000_trials_[0.0,0.01]_percentages.json"
    #python convert_json_to_csv.py "./jsons/V4OriginHijack_scenario_none_type_standard_policies_real_rov_20_conf_True_turnover_0_hash_False_probe_False_tunnel_None_relay_False_attackRelay_${attacker}_attacker_500_trials_full_percentages.json"
done
#done
done
done

mv jsons/*.csv csvs/
