#!/bin/bash

./rename.sh

declare -A dirs
dirs=( ["V4SubprefixHijackScenario"]="subprefix" ["SubprefixAutoImmuneScenario_scenario_direct_type"]="autoimmune-direct" ["SubprefixAutoImmuneScenario_scenario_indirect_type"]="autoimmune-indirect" ["real"]="rov-real" ["none"]="rov-none" ["True"]="attack-relay" ["False"]="no-attack-relay" ["50"]="prelim" ["500"]="final" )

for trials in 50 500
do
	# Create a Folder for each of the different settings
	for attack in V4SubprefixHijackScenario SubprefixAutoImmuneScenario_scenario_direct_type SubprefixAutoImmuneScenario_scenario_indirect_type 
	do
		for rov_setting in real none
		do
			# Move the no-relay setting
			for no_relay_zip_file in $( ls | grep ${trials}_trials| grep $attack | grep $rov_setting | grep None_relay )
			do
				unzip -o $no_relay_zip_file -d "${dirs[$trials]}/${dirs[$attack]}/${dirs[$rov_setting]}/no-relay/"
				unzip -o $no_relay_zip_file -d "mixed/${dirs[$attack]}/${dirs[$rov_setting]}/no-relay/"
			done
			
			# Move the results that use relays
			for relay_attack in True False 
			do
				for relay in akamai cloudflare verisign incapsula neustar five ten twenty
				do
					# First write out the 50 trial versions
					for relay_zip_file in $( ls | grep ${trials}_trials | grep $attack | grep ${rov_setting}_rov | grep ${relay_attack}_attackRelay | grep ${relay}_relay )
					do
						unzip -o $relay_zip_file -d "${dirs[$trials]}/${dirs[$attack]}/${dirs[$rov_setting]}/${dirs[$relay_attack]}/$relay/"
						unzip -o $relay_zip_file -d "mixed/${dirs[$attack]}/${dirs[$rov_setting]}/${dirs[$relay_attack]}/$relay/"
					done
				done
			done
		done
	done
done
