#!/bin/sh

seed=14;
run_name="trying_to_find_as_disconnect.py";
success=1;

while [ $success -eq 1 ] 
do
	echo "Running Python Script: $seed"
	python find_disconnected_avoid_list_asns.py $seed > /dev/null
	echo "Moved data"
	mv as_metadata.tsv ../data/${run_name}
	echo "Removed brackets"
	./remove_list_square_brackets.sh ../data/${run_name} > ../data/brackets_removed_${run_name}
	echo "Running R Script"
	Rscript avoid_list_traceback_asn_analysis.R "../data/brackets_removed_${run_name}" | grep Disconnected

	# Check if we found a diconnected avoid list asn outcome
	success=$?

	if [ $success -eq 1 ] 
	then
		echo "Deleted Data"
		rm ../data/${run_name} ../data/brackets_removed_${run_name}
		seed=$(($seed + 1))
	fi
done

