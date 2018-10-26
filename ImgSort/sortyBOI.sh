#!/usr/bin/env bash


for entry in ./$1/*.gif; # cycle through all *.gif (images) entries in directory
do
	FILE=$(basename $entry) # takes file name only from path
	INFO=(${FILE//-/ })
	#-------------------------------------------------------------
	# INFO is an array with the file name split with delimiter "-"
	# INFO contents:
	# INFO[0] = Weather Station Name
	# INFO[1] = Year
	# INFO[2] = Day
	# INFO[3] = Month
	# INFO[4] = Image No.
	#-------------------------------------------------------------

	if [ ! -d ./${INFO[0]}/${INFO[1]}/${INFO[3]}/${INFO[2]}/ ]
	then
		echo "the folder doesnt exist"
		echo "./${INFO[0]}/${INFO[1]}/${INFO[3]}/${INFO[2]}/ "
	fi

	echo "----------------------------"
	echo "MOVING FILE:" 
	echo $FILE
	
done

echo "exit Loop"
