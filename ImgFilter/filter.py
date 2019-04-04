#!/usr/bin/env python

#-----------------------------------------------------
# Imports

import cv2 as cv
import numpy as np
import sys

#-----------------------------------------------------
# Declarations and Constants

BGPath = "./run/background32.png"
ImgPath = sys.argv[1]
# list of possible colours of clouds picked up by radar images
cloudColours = [[153,0,102],[204,51,153],[153,2,255],[0,0,255],[0,102,255],[0,153,255],[0,204,255],[51,255,255],[0,102,0],[0,153,0],[0,204,0],[102,255,0],[255,153,0],[255,204,153]]

#-----------------------------------------------------

BG = cv.imread(BGPath, 1)   #read Background reference image
#cv.imshow("BG", BG)        # these sections may be uncommented to show each image after being
#cv.waitKey(0)              # read into the script


img = cv.imread(ImgPath, 1) #read image to be cleaned
#cv.imshow("image", img)
#cv.waitKey(0)

img_crop = img[270:301, 245:276]    # crop the image to 31x31 centred at the weather station
#cv.imshow("cropped", img_crop)
#cv.waitKey(0)

height, width = img_crop.shape[:2]  # store new dimensions of cropped image

# the following section will look at each pixel in the image and compare it to the list of
# cloud colours. Due to having three channels, each pixel colour must be checked individually
# preventing more efficient methods from being used. if a match is found a flag is set to
# indicate the pixel should be replaced. 

for i in range(height):
    for j in range(width):
        pix = img_crop[j,i,:]
        flag = 0 # flag for a matched cloud colour: 1 = match, 0 = no match
        for colour in cloudColours:
            if pix[0] == colour[0] and pix[1] == colour[1] and pix[2] == colour[2]:
                flag = 1
                break
        if flag == 0:
            img_crop[j,i,:] = BG[j,i,:]

#cv.imshow("clean", img_crop)
#cv.waitKey(0)

cv.imwrite("tmp.png", img_crop)# , CV_IMWRITE_PNG_COMPRESSION=0) #optional compression on write


