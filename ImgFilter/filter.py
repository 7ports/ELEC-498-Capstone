#!/usr/bin/env python

#-----------------------------------------------------
# Imports

import cv2 as cv
import numpy as np
import tools as t
import sys

#-----------------------------------------------------
# Declarations and Constants

land = [102,152,152]
sea = [102, 51, 51]
red = [0,0,255]
BGPath = "./run/background.png"
ImgPath = "./tmp/hollyrood.png"#sys.argv[1]
poi = open("points.txt", "r").read()   #get this to read in the points into a list insead of a string


#-----------------------------------------------------

BG = cv.imread(BGPath, 1)
cv.imshow("Background", BG)
cv.waitKey(0)

img = cv.imread(ImgPath, 1)
cv.imshow("image", img)
cv.waitKey(0)

height, width = img.shape[:2]

tmp = np.zeros((height, width, 3), np.uint8) #this is for testing which points the points.txt file contains

for i in poi:
    print(i)
    #tmp[i[0],i[1]] = BG[i[0],i[1]]

cv.imshow("tmp", tmp)
cv.waitKey(0)


#print(poi)

