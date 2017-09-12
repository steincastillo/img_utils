#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 22:43:39 2017

@author: Stein

*****************************************
*    Image Adjustable Thresholding      *
*                 V1.0                  *
*****************************************

Usage:
    python pthresholding.py -i <imageFile>
    
press <ESC> to exit
"""

# Import libraries
import cv2 as cv
import numpy as np
import os.path
import argparse

# Print header
print (__doc__)

# Define functions
def nothing(x):     # Dummy function for createTrackbar call
    pass

# Main loop
ap = argparse.ArgumentParser(description="Variable Thresholding")

ap.add_argument("-i",
                "--image",
                required=True,
                help ="Path to the image")

args = vars(ap.parse_args())

# Verify if the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify".format(args["image"]))
    exit(0)

image_orginal = cv.imread(args["image"])
image_gray = cv.cvtColor(image_orginal, cv.COLOR_BGR2GRAY)
image_blurred = cv.GaussianBlur(image_gray, (5, 5), 0)
image_blurred1 = image_blurred

# Create the image window
cv.namedWindow("image")

# Create trackbar
cv.createTrackbar("Threshold", "image", 3, 255, nothing)
th = 3
lth = 3

while True:
    cv.imshow("image", image_blurred)
    k = cv.waitKey(1) & 0xFF
    if k == 27:     # press <ESC> to quit
        break

    th = cv.getTrackbarPos("Threshold", "image")
    if th!=lth:
        lth = th
        print ("Thresholding level: {}".format(th))
        (t, image_blurred) = cv.threshold(image_blurred1, th, 255, cv.THRESH_BINARY)


cv.destroyAllWindows()
