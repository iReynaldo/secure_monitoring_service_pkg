#!/bin/bash

# Create directories for JSONs and CSVs
mkdir metadata
mkdir jsons

# Create a Folder for each of the different settings
for stage in prealpha alpha beta final mixed
do
    for attack in autoimmune-direct autoimmune-indirect subprefix superprefix prefix
    do
        for rov_setting in rov-real rov-none v4-mixed
        do
            mkdir -p $stage/$attack/$rov_setting/no-relay
            for relay_attack in attack-relay no-attack-relay
            do
                for relay in akamai cloudflare verisign incapsula neustar conglomerate five ten twenty forty fifty hundred
                do
                    mkdir -p $stage/$attack/$rov_setting/$relay_attack/$relay
                done
            done
        done
    done
done
