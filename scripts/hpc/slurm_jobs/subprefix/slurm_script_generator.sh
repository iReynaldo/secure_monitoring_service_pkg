#!/bin/bash

########################
# Constants
########################

export PYTHONHASHSEED=0
export HIJACK_SCENARIO="V4SubprefixHijackScenario"
export NUM_TRIALS=250

declare -A cpus
declare -A ram
cpus=( ["akamai"]="20" ["cloudflare"]="20" ["neustar"]="40" ["verisign"]="40" ["incapsula"]="20" ["conglomerate"]="40" ["five"]="40" ["ten"]="40" ["twenty"]="50" ["forty"]="50")
ram=( ["akamai"]="3" ["cloudflare"]="3" ["neustar"]="4" ["verisign"]="4" ["incapsula"]="3" ["conglomerate"]="4" ["five"]="4" ["ten"]="4" ["twenty"]="4" ["forty"]="4")

#######################
# Main 
#######################

# Initialize the submit_jobs script
rm submit_jobs.sh
touch submit_jobs.sh
chmod +x submit_jobs.sh
echo '#!/bin/sh' >> submit_jobs.sh
echo 'rm jobs.txt' >> submit_jobs.sh


# Create Script Files
for rov_setting in none
do
#----------------- File for Base Result for ROV and V1 Lite  --------------------
cat > standard_policies_rov_${rov_setting}.sh << EOF
#!/bin/bash
#SBATCH --partition=lo-core                   # Name of partition
#SBATCH --ntasks=20                           # Request Number of CPU cores
#SBATCH --mem-per-cpu=3G
#SBATCH --nodes=1
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=$PYTHONHASHSEED
cd ../../../
python __main__.py --num_trials $NUM_TRIALS --cpus 20 --python_hash_seed $PYTHONHASHSEED --rov_adoption ${rov_setting} --num_attackers 1 --policy rov v1lite --scenario $HIJACK_SCENARIO
EOF
# ----------------- File for Base Result for ROV and V1 Lite  --------------------

echo "sbatch standard_policies_rov_${rov_setting}.sh >> jobs.txt" >> submit_jobs.sh

# For metadata collection
# ----------------- Inner Loop Cannot be indented --------------------
for relay in neustar twenty                                                                                                                                    
do 
cat > meta_rov_${rov_setting}_overlay_${relay}.sh << EOF
#!/bin/bash
#SBATCH --partition=lo-core                   # Name of partition
#SBATCH --ntasks=${cpus[${relay}]}              # Request Number of CPU cores
#SBATCH --mem-per-cpu=${ram[$relay]}G
#SBATCH --nodes=1
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=$PYTHONHASHSEED
cd ../../../
python __main__.py --relay_asns ${relay} --num_trials $NUM_TRIALS --cpus ${cpus[${relay}]} --python_hash_seed $PYTHONHASHSEED --rov_adoption ${rov_setting} --num_attackers 1 --policy rovppo v4 --scenario $HIJACK_SCENARIO --collect_agg_as_metadata --tunnel_customers_traffic
EOF

echo "sbatch meta_rov_${rov_setting}_overlay_${relay}.sh >> jobs.txt" >> submit_jobs.sh

done
# ----------------- Inner Loop Cannot be indented --------------------

# Main data collection
# ----------------- Inner Loop Cannot be indented --------------------
for relay in neustar akamai cloudflare incapsula verisign conglomerate five ten twenty forty
do 
cat > rov_${rov_setting}_overlay_${relay}.sh << EOF
#!/bin/bash
#SBATCH --partition=lo-core                   # Name of partition
#SBATCH --ntasks=${cpus[${relay}]}              # Request Number of CPU cores
#SBATCH --mem-per-cpu=${ram[$relay]}G
#SBATCH --nodes=1
#SBATCH --mail-type=BEGIN,END,FAIL              # Event(s) that triggers email notification (BEGIN,END,FAIL,ALL)
#SBATCH --mail-user=reynaldo.morillo@uconn.edu  # Destination email address

# Setup pypy environment
source /home/rjm11010/miniconda3/etc/profile.d/conda.sh
conda activate py311

export PYTHONHASHSEED=$PYTHONHASHSEED
cd ../../../
python __main__.py --relay_asns ${relay} --num_trials $NUM_TRIALS --cpus ${cpus[${relay}]} --python_hash_seed $PYTHONHASHSEED --rov_adoption ${rov_setting} --num_attackers 1 --policy rovppo v4 --scenario $HIJACK_SCENARIO --tunnel_customers_traffic
EOF

echo "sbatch rov_${rov_setting}_overlay_${relay}.sh >> jobs.txt" >> submit_jobs.sh

done
# ----------------- Inner Loop Cannot be indented --------------------

done
