#!/usr/bin/env python

#import boopsboops as b
import numpy as np
import cv2 as cv

poi = []
img1 = cv.imread("./tmp/background.png", 1)
'''
img2 = img1.copy()
print(img1[100,200,:])
for i in range(255):
    for j in range(255):
        img1[0+i, 0+j, :] = [255-i,255-j,0+j] 
        img2[0+i, 0+j, :] = [255-i,255-j,0+i]
cv.imshow("img", img1)
cv.imshow("img2", img2)
cv.waitKey(0)
'''
height, width = img1.shape[:2]
'''
Ok so here what I want to try is to read the points.txt file and replace each
point with the background
'''
print(img1[100,100,:])
print(img1[300,90,:])
