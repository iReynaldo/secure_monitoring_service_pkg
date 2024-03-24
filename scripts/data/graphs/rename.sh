#!/bin/sh
  
#for file in $( ls | grep -E "*\_percentages.zip" )
#do
#    new_filename=$(echo $file | sed 's/\[0.01\,0.05\,0.1\,0.2\,0.4\,0.6\,0.8\,0.99\]/full/g' )
#    mv $file $new_filename
#done
#
## Fix none for Autoimmune attack type to indirect
#for file in $( ls | grep -E "SubprefixAutoImmuneScenario\_scenario\_none\_*" )
#do
#    new_filename=$(echo $file | sed 's/scenario\_none/scenario\_indirect/g' )
#    mv $file $new_filename
#done
#
## Fix None for attackRelay to False 
#for file in $( ls | grep -E "None\_attackRelay" )
#do
#    new_filename=$(echo $file | sed 's/None\_attackRelay/False\_attackRelay/g' )
#    mv $file $new_filename
#done

# Fix Minimum ROV confidence
for file in $( ls | grep -E "\_real\_rov\_0\_0" )
do
    new_filename=$(echo $file | sed 's/real\_rov\_0/real\_rov\_0\_conf/g' )
    mv $file $new_filename
done

