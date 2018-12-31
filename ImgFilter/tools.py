#!/usr/bin/env python
import cv2 as cv
import numpy as np



def replace(img, pt):
    height, width = img.shape[:2]
    
    r = 0
    g = 0
    b = 0
    for i in range(3):
        for j in range(3):
            if pt[0]+j >= height or pt[1]+i >= width:
                r += img[pt[0]-j, pt[1]-i,2]
                g += img[pt[0]-j, pt[1]-i,1]
                b += img[pt[0]-j, pt[1]-i,0]
            else:
                r += img[pt[0]+j, pt[1]+i, 2]
                g += img[pt[0]+j, pt[1]+i, 1]
                b += img[pt[0]+j, pt[1]+i, 0]
    return [b/9,g/9,r/9]

