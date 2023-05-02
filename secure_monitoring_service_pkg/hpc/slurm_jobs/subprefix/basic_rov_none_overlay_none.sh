#!/bin/bash
#SBATCH --partition=hi-core                  # Name of partition
#SBATCH --ntasks=100                            # Request Number of CPU cores
##SBATCH --mem=150G
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate v4sims

export PYTHONHASHSEED=0
python ../../python_scripts/rovpp_basic_subprefix_hijack.py none none false
