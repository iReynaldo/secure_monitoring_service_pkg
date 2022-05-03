#!/bin/sh

output_filename="all_tests.md"
output_dir="../overleaf_systest_doc/figs/system_test_images"

for hijack_type in v4_subprefix_hijack ;
do
    for sub_type in $(find $hijack_type -mindepth 1 -maxdepth 1 -type d) ;
    do  
        for sub_sub_type in $(find $sub_type -mindepth 1 -maxdepth 1 -type d) ;
        do
            for graph in $(find $sub_sub_type -mindepth 1 -maxdepth 1 -type d) ;
            do
                for policy_dir in $(find $graph -mindepth 1 -maxdepth 1 -type d | grep -v pycache ) ;
                do
                    for propapation_round_dir in $(find $policy_dir -mindepth 1 -maxdepth 1 -type d | grep -v pycache ) ;
                    do
                        for png in $(find $propapation_round_dir -mindepth 1 -maxdepth 1  | grep ".png$") ;
                        do
                            curr_output_dir=$output_dir/$propapation_round_dir;
                            echo $curr_output_dir
                            mkdir -p $curr_output_dir
                            # Extract the PNG
                            cp $png $curr_output_dir
                        done
                    done
                done
            done
        done
    done
done

