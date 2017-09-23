#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:43:30 2016
@author: Stein Castillo

**************************************
*            Auto Canny              *
*                                    *
*           Version: 1.2             *
**************************************

USAGE
    python auto_cannyv2.py -i [imageFile]
    python auto_cannyv2.py --image [imageFile]

Press any key to close
"""

#import libraries
import numpy as np
import argparse
import os.path 
import glob
import cv2

def auto_canny(image, sigma=0.33):
    #compute the median of a single channel pixel intensity
    v = np.median(image)
    
    #apply automatic canny edge detection using the computed medina
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    
    #return edged image
    return edged
    
#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", 
                "--image", 
                required = True,
                help ="path to the image")

args = vars(ap.parse_args())

# Print header
print (__doc__)

# Verify if the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify".format(args["image"]))
    exit(0)

#load the image, convert to grayscale and blur
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

#apply canny edge detection using wide, tight and auto thresholds
wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = auto_canny(blurred)

#show the images
cv2.imshow("Original", image)
cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
cv2.imshow("Edges", np.hstack([wide, tight, auto]))
cv2.waitKey(0)