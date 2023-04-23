#!/bin/sh

export PYTHONHASHSEED=0
\time -f "max_memory: %M, elapsed_time: %e" python __rov_main__.py ${1}
