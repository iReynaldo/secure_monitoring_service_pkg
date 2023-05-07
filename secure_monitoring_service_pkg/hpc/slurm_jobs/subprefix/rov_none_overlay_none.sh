#!/bin/bash
#SBATCH --partition=hi-core                   # Name of partition
#SBATCH --ntasks=20                            # Request Number of CPU cores
#SBATCH --mem=50G
#SBATCH --mem-per-cpu=3G
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=0
python ../../../__main__.py --policy rov v1lite --num_trials 50 --cpus 20 --python_hash_seed $PYTHONHASHSEED --rov_adoption none --num_attackers 5 --relay_asns none --scenario V4SubprefixHijackScenario
