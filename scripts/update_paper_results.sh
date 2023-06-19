#!/bin/sh

output_dir="../overleaf_paper/figures/results/final"
results_dir="../analysis/spyder/paper_plots"

# results
cp -R $results_dir/* $output_dir/

echo "Paper plots added to overleaf paper submodule"

cd ../overleaf_paper
echo "Pulling latest changes from Overleaf"
git pull origin master
git status
read -p "Ctrl-C to cancel git changes"
echo "Commiting changes"
git add .
git commit -m "Plot updates"
echo "Pushing changes to Overleaf"
git push origin master
