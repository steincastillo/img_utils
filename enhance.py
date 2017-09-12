#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*****************************************
Created on Sat Sep  2 10:20:25 2017
@author: Stein

*****************************************
*          Image Quick Enhance          *
*                 V1.2                  *
*****************************************

Adjustment parameters:
    alpha: Adjust contrast. Default value: 1.2
    beta: not used on this version. Default value: 0
    gamma: adjust brightness. Default value: 0

Usage: 
    python enhance.py -i <imageFile> -> Apply default values
    python enhance.py -i <imageFile> --alpha 2 --gamma 50
    python enhance.py -i <imageFile> -a 2 -g 50
    python enhance.py -i <imageFile> -a 1 -g 50 : only adjust brightness
    python enhance.py -i <imageFile> -a 2 : only adjust contrast

Examples:
    python enhance.py -i <imageFile> -a 0.5 -g 120 : X-ray effect
******************************************
"""

# Import libraries
import cv2 as cv
import os.path
import argparse
import numpy as np

print (__doc__)

# Parse the arguments
ap = argparse.ArgumentParser(description="Quick image enahancer")

ap.add_argument("-i",
                "--image",
                required=True, help ="Path to the image")

ap.add_argument("-a",
                "--alpha",
                required=False,
                default = 1.2,
                type = float,
                help = "alpha value - Contrast")

ap.add_argument("-b",
                "--beta",
                required=False,
                default = 0,
                type = float,
                help = "beta value - Not used")

ap.add_argument("-g",
                "--gamma",
                required = False,
                default = 0,
                type = float,
                help = "gamma value - Brightness")

args = vars(ap.parse_args())

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify.".format(args["image"]))
    exit(0)

# Open the image file
image = cv.imread(args["image"])

# Get image dimensions
height, width, _ = image.shape

# Unpack the editing parameters
alpha = float(args["alpha"])
beta  = float(args["beta"])
gamma = float(args["gamma"])

# result = ((image * alpha) + (np.zeros * beta) + gamma)
# alpha: changes the contrast of the image
# beta: Does nothing since it is multipied to an array of zeros
# gamma: changes the brigthness of the image
result = cv.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), beta, gamma)

# The next section was used to experiment with 2d convolution
#kernel = np.array([[-1,-1,-1], 
#                   [-1,9,-1], 
#                   [-1,-1,-1]])
    
#kernel = np.array([[0,-1, 0], 
#                   [-1,5,-1], 
#                   [0,-1, 0]])
    
#result = cv.filter2D(image, -1, kernel)

print ("Press [s] to save")
print ("Press any key to quit")

# Resize and present original image
image = cv.resize(image, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.imshow("Original", image)
#cv.resizeWindow("Original", int(width/2), int(height/2))

# Present equalized image 
cv.namedWindow("Enhanced", cv.WINDOW_NORMAL)
cv.imshow("Enhanced", result)

key = cv.waitKey(0) &0xFF

# Save the file?
if key == ord("s"):
    # Get new file name
    name = args["image"].split(".")
    filename = input ("File name: ")
    savefile = filename + "." + name[1]
    # Check that the file does not exist
    if (os.path.isfile(savefile)):              
        print ("[ERROR] File {} already exist. Please verify".format(savefile))
        print ("[INFO] File not saved!")
    else:
        print ("Saving: ", savefile)
        cv.imwrite(savefile, result)
else:
    print ("[INFO] File not saved!")
    
cv.destroyAllWindows()
