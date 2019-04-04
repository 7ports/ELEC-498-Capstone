#!/usr/bin/env python
#---------------------------------------------

import numpy as np
import h5py as h
import cv2 as cv

#---------------------------------------------
# This file creates an hdf5 file from the clean directory
# The structure of the file is as follows:
# ROOT/year/month/day/hour/rotation
#---------------------------------------------
f = h.File('data.hdf5', 'w')    #create hdf5 file object

monthkey = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}


for year in range(2008,2018):
    for month in monthkey:
        for day in range(1,29):
            for hour in range(24):
                path = "./clean/Halifax-"+ str(year) +"-"+ str(day) +"-"+ str(month) +"-"+ str(hour) +".png-clean.png"
                print(path)
                try:
                    img = cv.imread(path, 1) #0 rotation
                    
                    rot_mat = cv.getRotationMatrix2D((16,16),90,1)

                    img1=cv.warpAffine(img, rot_mat, (31, 31)) #90 degrees
                    img2=cv.warpAffine(img1, rot_mat, (31, 31)) #180 degrees
                    img3=cv.warpAffine(img2, rot_mat, (31, 31)) #270 degrees

                    tmp = f.create_group(str(year) + '/' + month + '/' + str(day) + '/' + str(hour) + "-0")
                    tmp.create_dataset(str(year) + "-" + month + "-" + str(day) + "-" + str(hour) + "-0", data=img)
                    tmp = f.create_group(str(year) + '/' + month + '/' + str(day) + '/' + str(hour) + "-1")
                    tmp.create_dataset(str(year) + "-" + month + "-" + str(day) + "-" + str(hour) + "-1", data=img1)
                    tmp = f.create_group(str(year) + '/' + month + '/' + str(day) + '/' + str(hour) + "-2")
                    tmp.create_dataset(str(year) + "-" + month + "-" + str(day) + "-" + str(hour) + "-2", data=img2)
                    tmp = f.create_group(str(year) + '/' + month + '/' + str(day) + '/' + str(hour) + "-3")
                    tmp.create_dataset(str(year) + "-" + month + "-" + str(day) + "-" + str(hour) + "-3", data=img3)

                except:
                    print("no image found")

