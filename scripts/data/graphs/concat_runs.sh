#!/bin/sh

prefix=$1
suffix=$2
new_filename=${prefix}_full_${suffix}

cat `ls -1 | grep -E "${prefix}_\[[0-9.]+\]_${suffix}"` | sort -r | uniq > $new_filename
echo $new_filename

mv $new_filename ./metadata

# Command to remove the concatenated files
# Run the following command on it's own outside the script
# !!!!!!!!!!!!!!!!!! Note this could also delete the file that was 
# just made, so make sure it's removed from the current directory
#
# ls -1 | grep 12000 | grep csv | xargs rm
