#!/bin/sh

echo "Splitting reports into python modules"
split -e -l 7 -a 3 -d --additional-suffix=".py" ${1}
# compute number of files
num_modules=$(ls | grep -E "^x[0-9]*" | wc -l)
adjusted_num_modules=$(($num_modules - 1))
echo "Num Modules: ${adjusted_num_modules}"
echo "Running AvoidList and TSV creator"
pypy create_avoid_list_tsv.py $adjusted_num_modules
echo "Removing split report modules"
rm x*.py

