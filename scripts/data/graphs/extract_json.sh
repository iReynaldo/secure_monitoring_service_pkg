#!/bin/sh

# Args
zip_file=$1

# Create a tmp place to unzip file
mkdir unzip_place
cd unzip_place

# Unzip
unzip ../$zip_file

# Extract the JSON
mv results.json ../jsons/"${zip_file%.*}".json

# Clean up
cd ..
rm -rf unzip_place
