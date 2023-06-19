#!/bin/bash

# Create a Folder for each of the different settings
for stage in prelim final mixed
do
    for attack in autoimmune-direct autoimmune-indirect subprefix superprefix
    do
        for rov_setting in rov-real rov-none
        do
            mkdir -p $stage/$attack/$rov_setting/no-relay
            for relay_attack in attack-relay no-attack-relay
            do
                for relay in akamai cloudflare verisign incapsula neustar five ten twenty
                do
                    mkdir -p $stage/$attack/$rov_setting/$relay_attack/$relay
                done
            done
        done
    done
done
