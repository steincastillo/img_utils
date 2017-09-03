#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 10:20:25 2017
@author: Stein

*****************************************
*          Image Quick Enhance          *
*                 V1.2                  *
*****************************************

Adjustment parameters:
    alpha: Adjust contrast. Default value: 1.5
    beta: not used on this version. Default value: 0
    gamma: adjust brightness. Default value: 0

Usage: 
    python enhance.py -i <imageFile> -> Apply default values
    python enhance.py -i <imageFile> --alpha 2 --beta 50
    python enhance.py -i <imageFile> -a 2 -b 50
    python enhance.py -i <imageFile> -a 1 -b 50 : only adjust brigthness
    python enhance.py -i <imageFile> -a 2 : only adjust contrast

Examples:
    python enhance.py -i <imageFile> -a 0.5 -b 120 : X-ray effect
    
"""

import cv2 as cv
import os.path
import argparse
import numpy as np

print (__doc__)

# Parse the arguments
ap = argparse.ArgumentParser(description="Quick image enahancer")
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
ap.add_argument("-a", "--alpha", required=False, default = 1.5, 
                help = "alpha value")
ap.add_argument("-b", "--beta", required=False, default = 0,
                help = "beta value")
ap.add_argument("-g", "--gamma", required = False, default = 0, 
                help = "gamma value")
args = vars(ap.parse_args())

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

image = cv.imread(args["image"])

alpha = float(args["alpha"])
beta = float(args["beta"])
gamma = float(args["gamma"])

result = cv.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), beta, gamma)
#kernel = np.array([[-1,-1,-1], 
#                   [-1,9,-1], 
#                   [-1,-1,-1]])
    
kernel = np.array([[0,-1, 0], 
                   [-1,5,-1], 
                   [0,-1, 0]])
    
#result = cv.filter2D(image, -1, kernel)

cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.imshow("Original", image)
cv.namedWindow("Enhanced", cv.WINDOW_NORMAL)
cv.imshow("Enhanced", result)

key = cv.waitKey(0) &0xFF

cv.destroyAllWindows()
