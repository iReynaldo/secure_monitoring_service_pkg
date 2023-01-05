#!/bin/sh

configs_to_run=$1

for config in $1
do
    export PYTHONHASHSEED=0;
    ./deterministic_pytest -v --view --overwrite -k Config${config}
done
