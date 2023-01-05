#!/bin/sh

export PYTHONHASHSEED=0
\time -f "max_memory: %M, elapsed_time: %e" pypy __main__.py
