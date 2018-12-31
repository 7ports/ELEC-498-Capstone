#!/usr/bin/env bash
#TODO: 
# - extract file name w/out .png extension
# - save image as tmp.png in boopsboops.py
#
path=$1

for i in $path*.png;
do
	file=$(basename $i)
	#python boopsboops.py $path$file
	mkdir clean
	mv tmp.png ./clean/$name-clean.png
done

