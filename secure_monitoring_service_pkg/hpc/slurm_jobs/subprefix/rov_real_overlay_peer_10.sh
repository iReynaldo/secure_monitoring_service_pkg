#!/bin/bash
#SBATCH --partition=hi-core                   # Name of partition
#SBATCH --ntasks=12                            # Request Number of CPU cores
#SBATCH --mem=154G
#SBATCH --mem-per-cpu=12G
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=0
python ../../../__main__.py --relay_asns ten --num_trials 50 --cpus 20 --python_hash_seed $PYTHONHASHSEED --rov_adoption real --num_attackers 5 --scenario V4SubprefixHijackScenario
