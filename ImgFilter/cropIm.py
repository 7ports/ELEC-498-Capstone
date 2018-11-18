import numpy as np
import cv2 as cv


img = cv.imread('hollyrood.png', 1) 
cv.imshow('image', img)
cv.waitKey(0)


imgCrop = img[0:500, 0:485]
cv.imshow('cropped', imgCrop)
cv.waitKey(0)
