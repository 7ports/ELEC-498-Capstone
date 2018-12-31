#!/usr/bin/env python
import cv2 as cv
import numpy as np
import tools as t
import sys
land = [102,152,152]
sea = [102, 51, 51]
red = [0,0,255]
path = sys.argv[1]

img = cv.imread(path, 1)
cv.imshow("image", img)
cv.waitKey(0)
poi = []
imgBG = img.copy()

width, height = imgBG.shape[:2]
#print(width, height)

for i in range(height):
    for j in range(width):
        pix1=img[j,i,:]-red
        pix2=img[j,i,:]-[255,255,255]
        pix3=img[j,i,:]
        if abs(pix1[0]) < 60 and abs(pix1[1]) < 60 and abs(pix1[2]) < 50:
            imgBG[j,i,:] = img[j,i,:]
            poi.append([j,i])
        elif abs(pix2[0]) < 25 and abs(pix2[1]) < 20 and abs(pix2[2]) < 25:
            imgBG[j,i,:] = img[j,i,:]
            poi.append([j,i])
        elif abs(pix3[0]) < 15 and abs(pix3[1]) < 10 and abs(pix3[2]) < 15:
            imgBG[j,i,:] = [255,255,255]
            poi.append([j,i])
        else:
            imgBG[j,i,:] = [0,0,0]


cv.imshow('bg', imgBG)
cv.waitKey(0)
#print(poi)

tmp = img - imgBG #img.copy()
#cv.imshow("rmp", tmp)
#cv.waitKey(0)
'''
#this part does replaces the poi value with either land or sea colour (gets rid of rings)
for point in poi:
    if point[0]+1 >= width or point[1]+1 >= height:
        val = tmp[point[0]-1, point[1]-1, :]
    else:
        val = tmp[point[0]+1, point[1]+1, :]
    if val[0] == land[0] and val[1] == land[1] and val[2] == land[2]:
        tmp[point[0], point[1], :] = land
    else: 
        tmp[point[0], point[1], :] = sea 
 
cv.imshow("tmp", tmp)
cv.waitKey(0)
'''

for i in range(3):
    for point in poi:
        tmp[point[0],point[1],:] = t.replace(tmp,[point[0],point[1]])

'''
cv.imshow("tmp", tmp)
cv.waitKey(0)

'''
'''
tmp = img.copy()

for i in range(height):
    for j in range(width):
        pixel = tmp[j,i,:]-red
        if abs(pixel[0]) < 5 and abs(pixel[1]) < 5 and abs(pixel[2]) < 10:
            tmp[j,i,:] = t.replace(tmp, [j,i])
'''          
cv.imshow('tmp', tmp)
cv.waitKey(0)


