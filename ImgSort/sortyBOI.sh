#!/usr/bin/env bash


IPATH="$1"
echo "-----------------------SORTING IMAGES------------------------"
echo "."
for entry in $IPATH/*.gif; # cycle through all *.gif (images) entries in directory
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

	# Constructing File Path in variable FPATH
	FPATH="./${INFO[0]}/${INFO[1]}/${INFO[3]}/${INFO[2]}/ "
	echo $FPATH

	# Check if the directory for the file has been created
	if [ ! -d $FPATH ]   
	then
		# If directory cannot be found, create the folder and
		# all other parent directories required. 
		echo "The folder: $FPATH"
		echo "could not be found... Creating directory"
		mkdir -p $FPATH
	fi
	
	# Move the files to the specified directory they belong to
	echo "------------------------------------------------------------"
	echo "."
	echo "MOVING FILE:  $FILE"
	echo "."
	mv $IPATH/$FILE $FPATH
done

echo "----------------------PROCESS COMPLETE----------------------"
echo "."
echo "DISPLAYING CONTENTS OF FOLDER: $FPATH"
echo "------------------------------------------------------------"
echo "."
ls $FPATH
echo "."
echo "------------------------------------------------------------"
