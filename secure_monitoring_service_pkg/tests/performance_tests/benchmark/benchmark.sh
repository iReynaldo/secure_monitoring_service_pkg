#!/bin/sh

tag=${1}
profile_file="$(hostname)_$(date -Iminutes).profile"
pypy -m cProfile -o $profile_file probe.py --tag $tag
mv $profile_file ./profiles/
