#!/bin/sh

cpu=${1}
profile_file="$(hostname)_$(date -Iminutes).profile"
pypy -m cProfile -o $profile_file probe.py --cpus ${cpu}
mv $profile_file ./profiles/
