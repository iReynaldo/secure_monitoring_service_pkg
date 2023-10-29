#!/bin/sh

sbatch rov_none_overlay_none.sh
sbatch rov_real_overlay_none.sh
sbatch rov_real_overlay_akamai.sh 
sbatch rov_real_overlay_cloudflare.sh
sbatch rov_real_overlay_incapsula.sh
sbatch rov_real_overlay_neustar.sh
sbatch rov_real_overlay_verisign.sh
sbatch rov_real_overlay_peer_5.sh
sbatch rov_real_overlay_peer_10.sh
sbatch rov_real_overlay_peer_20.sh
