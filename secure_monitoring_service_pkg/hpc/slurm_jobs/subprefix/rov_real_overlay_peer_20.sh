#!/bin/bash
#SBATCH --partition=hi-core                   # Name of partition
#SBATCH --ntasks=8                            # Request Number of CPU cores
#SBATCH --mem=186G
#SBATCH --mem-per-cpu=22G
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=0
python ../../../__main__.py --relay_asns twenty --num_trials 50 --cpus 5 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 5 --scenario V4SubprefixHijackScenario
