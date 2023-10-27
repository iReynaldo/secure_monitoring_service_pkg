#!/bin/sh

export PYTHONHASHSEED=1
\time -f "max_memory: %M, elapsed_time: %e" python peer_arg_main.py ${1}
