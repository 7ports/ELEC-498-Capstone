import numpy as np
import cv2 as cv
import sys

path = sys.argv[1]
print(path)

img = cv.imread(path, 1) 
cv.imshow('image', img)
cv.waitKey(0)


imgCrop = img[0:500, 0:485]
cv.imshow('cropped', imgCrop)
cv.waitKey(0)
