#!/usr/bin/env bash
# - extract file name w/out .png extension
#
path=$1						#path to image dir
mkdir ~/clean					#make a directory to place clean files in
find $1 -print0 | while IFS= read -r -d '' i	#recursive search of dir for subdir and images
do
	if [ ! -d "$i" ]			#if not a dir
       	then	
		# This section extracts the filename and converts the *.jpg to tmp.png to load into
		# filter.py which is then used to clean each image. After, the file is then named
		# and moved to the clean directory.
		file=$(basename $i)				#extract filename
		echo $path$file					#User info and monitoring
	#	convert $path$file ~/ELEC-498-Capstone/ImgFilter/run/tmp.png
		python filter.py $path$file #~/ELEC-498-Capstone/ImgFilter/run/tmp.png
		mv ~/ELEC-498-Capstone/ImgFilter/tmp.png ~/clean/${file%.jpg}-clean.png
	#	rm ~/ELEC-498-Capstone/ImgFilter/run/tmp.png
	fi	
done

