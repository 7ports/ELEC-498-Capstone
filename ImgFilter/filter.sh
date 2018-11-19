#!/usr/bin/env bash

path=$1

for i in $path*.png;
do
	file=$(basename $i)
	python cropIm.py $path$file 
done
