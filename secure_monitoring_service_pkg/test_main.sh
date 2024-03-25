#!/bin/bash
#SBATCH --partition=hi-core                   # Name of partition
#SBATCH --ntasks=20                            # Request Number of CPU cores
#SBATCH --mem-per-cpu=3G
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
#source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
#conda activate py311

export PYTHONHASHSEED=0
#cd ../../../
#python __main__.py --percentages 0.99 --relay_asns neustar --policy v1lite --num_trials 2 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 5 --scenario V4SubprefixHijackScenario --attack_relays True
#python __main__.py --percentages 0.99 --policy v4k2 --relay_asns five --num_trials 10 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 5 --scenario V4SubprefixHijackScenario --attack_relays True


# TODO: solve error produced here
#   The error is in the error is in trusted server trying to use cached information about other avoid lists
#python __main__.py --percentages 0.1 --relay_asns cloudflare --num_trials 10 --policy v4k2 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 5 --scenario SubprefixAutoImmuneScenario --autoimmune_attack_type direct --attack_relays True

# Understand weird 20% for successful connections and disconnections for direct autoimmune
# Cannot use multiprocessing for debugging this issue, because the logger depends on serial execution
#python __main__.py --percentages 0.1 0.4 0.8 --num_trials 20 --policy v4k2 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --scenario SubprefixAutoImmuneScenario --autoimmune_attack_type direct
#python __main__.py --percentages 0.1 --relay_asns cloudflare --num_trials 5 --policy v4k2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --scenario SubprefixAutoImmuneScenario --autoimmune_attack_type direct --attack_relays False

# Check if there's hidden hijacks for the subprefix hijack scenario with CDNs at 1%, 5%, and 10%
#python __main__.py --relay_asns cloudflare --num_trials 5 --policy v4 --cpus 3 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 1.0 --num_attackers 5 --scenario V4SubprefixHijackScenario --allow_rov_turnover --tunnel_customers_traffic

#python __main__.py --relay_asns akamai --num_trials 1 --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --scenario SubprefixAutoImmuneScenario --autoimmune_attack_type direct

#python __main__.py --percentages 0.1 0.5 0.99 --relay_asns akamai --policy rov v1lite v4k5 --cpus 3 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --scenario V4SuperprefixPrefixHijack

# Seeding conflict error
#python __main__.py --relay_asns neustar --policy v4k5 --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --scenario V4SubprefixHijackScenario
#python __main__.py --relay_asns neustar --policy v4k5 --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --scenario V4SubprefixHijackScenario --attack_relays True

#python __main__.py --relay_asns neustar --policy rovppo --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --scenario V4SubprefixHijackScenario
#python __main__.py --relay_asns akamai --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --policy rov v1lite rovppo --probe_data_plane True --scenario V4SubprefixHijackScenario

#python __main__.py --percentages 0.1 0.5 0.8 --relay_asns five --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --replace_rov_ases_with v4 --num_attackers 1 --policy rov v1lite --scenario V4SubprefixHijackScenario

#python __main__.py --percentages 0.1 0.5 0.8 --relay_asns five --num_trials 2 --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --policy v4 --scenario V4SubprefixHijackScenario --attack_relays True
#python __main__.py --percentages 0.1 --relay_asns conglomerate --num_trials 10 --cpus 5 --python_hash_seed 0 --rov_adoption real --num_attackers 1 --policy v4 --scenario V4SubprefixHijackScenario --attack_relays True --collect_avoid_list_metadata True
#python __main__.py --num_trials 100 --cpus 4 --python_hash_seed 0 --num_attackers 1 --policy rov v1lite --scenario V4SubprefixHijackScenario

#python __main__.py --num_trials 3 --cpus 1 --python_hash_seed 0 --num_attackers 1 --relay_asns akamai --policy rov v1lite rovppo v4 --scenario V4PrefixHijackScenario

#python __main__.py --num_trials 2 --policy rovppo --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --scenario V4SubprefixHijackScenario --collect_agg_as_metadata

#python __main__.py --num_trials 2 --policy rovppo --relay_asns akamai --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 1 --scenario V4SubprefixHijackScenario --tunnel_customers_traffic

#python __main__.py --num_trials 2 --policy v1lite rov --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 0.9 --num_attackers 1 --scenario V4SubprefixHijackScenario

#python __main__.py --num_trials 2 --policy artemis --cpus 2 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 0.9 --num_attackers 1 --scenario ArtemisSubprefixHijackScenario
#python __main__.py --relay_asns cloudflare --num_trials 5 --policy artemis --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --scenario ArtemisSubprefixHijackScenario --allow_rov_turnover

#python __main__.py --relay_asns cloudflare --num_trials 2 --policy artemis --cpus 3 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 1 --scenario ArtemisSubprefixHijackScenario --fightback_cdn_only

#python __main__.py --relay_asns neustar --num_trials 2 --policy artemis --cpus 1 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 1 --scenario RelayPrefixHijack --fightback_cdn_only

#python __main__.py --percentages 0.5 --relay_asns five --num_trials 2 --cpus 1 --python_hash_seed 0 --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --policy v4 --scenario V4OriginHijack --allow_rov_turnover --attack_relays

#python __main__.py --relay_asns cloudflare --num_trials 5 --cpus 4 --python_hash_seed 0 --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --policy artemis --scenario ArtemisSubprefixHijackScenario --attack_relays
#python __main__.py --relay_asns verisign --num_trials 10 --cpus 4 --python_hash_seed 0 --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --policy v4 --scenario V4SubprefixHijackScenario --attack_relays --attack_relays_type origin_hijack
#python __main__.py --relay_asns cloudflare --num_trials 10 --cpus 4 --python_hash_seed 0 --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --policy v4 --scenario V4SubprefixHijackScenario --attack_relays

python __main__.py --relay_asns verisign --num_trials 10 --cpus 4 --python_hash_seed 0 --rov_adoption real --rov_adoption_min_conf 0.2 --num_attackers 5 --policy artemis --scenario ArtemisSubprefixHijackScenario --attack_relays --attack_relays_type origin_hijack
