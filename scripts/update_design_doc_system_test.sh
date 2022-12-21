#!/bin/sh

output_dir="../overleaf_design_doc/figures/system_tests"
system_test_dir="../secure_monitoring_service_pkg/tests/engine_tests/engine_test_outputs"

# System Test 1
cp $system_test_dir/142/ground_truth_1.2.1.0_24.gv.png $output_dir/config-142.png
cp $system_test_dir/143/ground_truth_1.2.1.0_24.gv.png $output_dir/config-143.png
cp $system_test_dir/144/ground_truth_1.2.1.0_24.gv.png $output_dir/config-144.png
# System Test 2
cp $system_test_dir/145/ground_truth_1.2.1.0_24.gv.png $output_dir/config-145.png
cp $system_test_dir/146/ground_truth_1.2.1.0_24.gv.png $output_dir/config-146.png
cp $system_test_dir/147/ground_truth_1.2.1.0_24.gv.png $output_dir/config-147.png
# System Test 3
cp $system_test_dir/149/ground_truth_1.2.1.0_24.gv.png $output_dir/config-149-1.png
cp $system_test_dir/149/ground_truth_1.2.2.0_24.gv.png $output_dir/config-149-2.png
cp $system_test_dir/148/ground_truth_1.2.1.0_24.gv.png $output_dir/config-148-1.png
cp $system_test_dir/148/ground_truth_1.2.2.0_24.gv.png $output_dir/config-148-2.png

echo "System tests added to overleaf design doc submodule"

cd ../overleaf_design_doc
echo "Pulling latest changes from Overleaf"
git pull origin master
git status
read -p "Ctrl-C to cancel git changes"
echo "Commiting changes"
git add .
git commit -m "System test updates"
echo "Pushing changes to Overleaf"
git push origin master
