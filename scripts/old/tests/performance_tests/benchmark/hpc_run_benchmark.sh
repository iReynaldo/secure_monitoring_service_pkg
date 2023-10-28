#!/bin/bash
#SBATCH --partition=general                   # Name of partition
#SBATCH --ntasks=12                            # Request Number of CPU cores
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate v4sims

./run_benchmarks.sh V4SubprefixHijackScenario updated-subprefix
