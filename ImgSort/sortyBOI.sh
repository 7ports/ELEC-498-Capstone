#!/usr/bin/env bash


for i in ./$1/*.gif;
do
	echo $i
	FILE=$(basename $i)
	echo $FILE
	INFO=(${FILE//-/ })
	echo ${INFO[0]}
	echo ${INFO[1]}
done

echo "exit Loop"
