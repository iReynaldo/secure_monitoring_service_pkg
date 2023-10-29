#!/bin/sh

commit_message="Plot updates"

# Check if commit message given
if [ $# -eq 1 ]
then
    commit_message=$1
fi

output_dir="../../overleaf_bgp_immunity/figures/results/new"
results_dir="./analysis/spyder/immunity_paper_plots"

# results
cp -R $results_dir/* $output_dir/

echo "Paper plots added to overleaf paper repo"

cd ../overleaf_bgp_immunity
echo "Pulling latest changes from Overleaf"
git pull origin master
git status | more
read -p "Ctrl-C to cancel git changes"
echo "Commiting changes"
git add .
git commit -m "${commit_message}"
echo "Pushing changes to Overleaf"
git push origin master
