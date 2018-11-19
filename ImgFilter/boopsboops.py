import cv2 as cv
import numpy as np


img = cv.imread('./tmp/background.png', 1)
cv.imshow("image", img)
cv.waitKey(0)


imgBG = img.copy()

width, height = imgBG.shape[:2]
#print(width, height)

for i in range(height):
    for j in range(width):
        pix1=img[j,i,:]-[0,0,255]
        pix2=img[j,i,:]-[255,255,255]
        if abs(pix1[0]) < 60 and abs(pix1[1]) < 60 and abs(pix1[2]) < 50:
            imgBG[j,i,:] = img[j,i,:]
        elif abs(pix2[0]) < 25 and abs(pix2[1]) < 20 and abs(pix2[2]) < 25:
            imgBG[j,i,:] = img[j,i,:]
        else:
            imgBG[j,i,:] = [0,0,0]


cv.imshow('bg', imgBG)
cv.waitKey(0)
                
