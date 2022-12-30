#!/bin/bash

overleaf_dir="../overleaf_results_doc"
output_dir="${overleaf_dir}/figs/results"
graphs_zip_file="set_with_args_loop_below"
usage_information="script usage: $(basename \${0}) [-n graph-zip-file] [-u graph-zip-file]"

# Based on the flag entered do the following for the updates
while getopts 'n:u:h' OPTION; do
  case "$OPTION" in
    n)  # Save old PDF and Create a new PDF
	  echo "New PDF feature is not Implemented yet"
      graphs_zip_file=$OPTARG
      ;;
    u)  # Update the current PDF
      echo "Updating current PDF"
      graphs_zip_file=$OPTARG
      ;;
	h)  # Help (Usage information)
	  echo $usage_information
	  ;;
    ?)
      echo $usage_information >&2
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

# Unzip results
unzip $graphs_zip_file
# Copy over all results files
mv *.png $output_dir
mv results.json $output_dir

# Graphs copied over
echo "Graphs copied over to overleaf results dir"

# Pull Latest Changes
cd ../overleaf_results_doc
echo "Pulling latest changes from Overleaf"
git pull origin master
git status


# Check the status of the and confirm changes
git status
read -p "Ctrl-C to cancel git changes"

# Commit and Push changes
echo "Commiting changes"
git add .
git commit -m "System test updates"
echo "Pushing changes to Overleaf"
git push origin master

