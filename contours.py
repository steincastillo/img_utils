#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:43:39 2017
Updated on 

@author: Stein

***********************************
*       Contours Detection        *
*              V1.1               *
***********************************
"""

# Import libraries
import argparse
import os.path 
import numpy as np
import cv2 as cv

# Define color constants
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)


def auto_canny(image, sigma=0.33):
    #compute the median of a single channel pixel intensity
    v = np.median(image)
    
    #apply automatic canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1 + sigma) * v))
    edged = cv.Canny(image, lower, upper)
    
    #return edged image
    return edged

ap = argparse.ArgumentParser(description="Find image contours")
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

image_original = cv.imread(args["image"])
image = cv.cvtColor(image_original, cv.COLOR_BGR2GRAY)

# Pre-process image


img_filt = cv.medianBlur(image, 5)
#img_th = auto_canny(img_filt)
img_th = cv.threshold(img_filt, 60, 255, cv.THRESH_BINARY)[1]
#img_th = cv.adaptiveThreshold(img_filt,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
im2, contours, hierarchy = cv.findContours(img_th, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.namedWindow(str(args["image"]), cv.WINDOW_NORMAL)
cv.imshow(str(args["image"]), image)

#cv.drawContours(image_orginal,contours,-1,(128,255,0),1)
cv.drawContours(image_original,contours,-1,BLUE,1)
display = cv.imshow("Objects",image_original)
print ("Number of dectected elements: {}".format(len(contours)))
wait_time = cv.waitKey(0)
cv.destroyAllWindows()

#plt.imshow(img_orig)