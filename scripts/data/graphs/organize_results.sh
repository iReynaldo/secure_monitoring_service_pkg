#!/bin/bash

./rename.sh

declare -A dirs
dirs=( ["V4SuperprefixPrefixHijack"]="superprefix" ["V4SubprefixHijackScenario"]="subprefix" ["SubprefixAutoImmuneScenario_scenario_direct_type"]="autoimmune-direct" ["SubprefixAutoImmuneScenario_scenario_indirect_type"]="autoimmune-indirect" ["V4PrefixHijackScenario"]="prefix" ["ArtemisSubprefixHijackScenario"]="artemis-subprefix" ["RelayPrefixHijack"]="relay-prefix" ["V4OriginHijack"]="V4OriginHijack" ["real"]="rov-real" ["none"]="rov-none" ["v4"]="v4-mix" ["True"]="attack-relay" ["False"]="no-attack-relay" ["50"]="prealpha" ["500"]="alpha" ["2000"]="beta" [8000]="final")

for trials in 50 500 1000 2000 4000 8000 16000
do
	# Create a Folder for each of the different settings
	for attack in V4SubprefixHijackScenario SubprefixAutoImmuneScenario_scenario_direct_type SubprefixAutoImmuneScenario_scenario_indirect_type V4SuperprefixPrefixHijack V4PrefixHijackScenario ArtemisSubprefixHijackScenario RelayPrefixHijack V4OriginHijack
	do
		for rov_setting in real none v4
		do
			# Move the no-relay setting
			for no_relay_zip_file in $( ls | grep conf | grep -E '500|1000|2000|4000|8000|16000' | grep ${trials}_trials| grep $attack | grep $rov_setting | grep None_relay | grep zip )
			do
				#unzip -o $no_relay_zip_file -d "${dirs[$trials]}/${dirs[$attack]}/${dirs[$rov_setting]}/no-relay/"
				#unzip -o $no_relay_zip_file -d "mixed/${dirs[$attack]}/${dirs[$rov_setting]}/no-relay/"
                ./extract_json.sh $no_relay_zip_file
			done
			
			# Move the results that use relays
			for relay_attack in True False 
			do
				for relay in akamai cloudflare verisign incapsula conglomerate neustar five ten twenty forty fifty hundred
				do
					# First write out the 50 trial versions
					for relay_zip_file in $( ls | grep conf | grep -E '500|1000|2000|4000|8000|16000' | grep ${trials}_trials | grep $attack | grep ${rov_setting}_rov | grep ${relay_attack}_attackRelay | grep ${relay}_relay | grep zip )
					do
						#unzip -o $relay_zip_file -d "${dirs[$trials]}/${dirs[$attack]}/${dirs[$rov_setting]}/${dirs[$relay_attack]}/$relay/"
						#unzip -o $relay_zip_file -d "mixed/${dirs[$attack]}/${dirs[$rov_setting]}/${dirs[$relay_attack]}/$relay/"
                        ./extract_json.sh $relay_zip_file 
					done
				done
			done
		done
	done
done

# Organize CSV Files
echo "Organizing Metadata"
./move_metadata.sh  # This script was also disabled from within

