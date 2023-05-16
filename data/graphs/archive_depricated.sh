#!/bin/sh

mkdir -p depricated

# Move relay results that used relays incorrectly May 12, 2023
mv *akamai* depricated/
mv *cloudflare* depricated/
mv *verisign* depricated/
mv *incapsula* depricated/
mv *neustar* depricated/
mv *five* depricated/
mv *ten* depricated/
mv *twenty* depricated/
