#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*****************************************
Created on Sun Sep  3 13:02:21 2017

@author: Stein

*****************************************
*       Color Image Equalization        *
*                 V1.0                  *
*****************************************

Usage:
    python coloreq.py -i <imageFile>
    python coloreq.py --image <imageFile>
*****************************************
"""

# Import libraries
import cv2 as cv
import os.path
import argparse

# Display the header
print (__doc__)

# Parse the arguments
ap = argparse.ArgumentParser(description="Color image equalizer")

ap.add_argument("-i",
                "--image",
                required=True,
                help ="Path to the image")

args = vars(ap.parse_args())

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify.".format(args["image"]))
    exit(0)
 
# Open the image
image = cv.imread(args["image"])

# Verify input image is a color image
height, width, channels = image.shape
if channels < 3 :
    print ("[ERROR] Input file must be a color image. Please verify\n")
    exit(0)

# Convert the image to YUV color space
img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)

# equalize the histogram of the Y channel - Intensity channel
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

# Resize original image
image = cv.resize(image, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)

print ("Press [s] to save")
print ("Press any key to quit")

# Display the original and equalized images
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.imshow("Original", image)
#cv.resizeWindow("Original", int(width/2), int(height/2))
cv.namedWindow("Equalized", cv.WINDOW_NORMAL)
cv.imshow("Equalized", img_output)

key = cv.waitKey(0)

# Save the file?
if key == ord("s"):
    # Get new file name
    name = args["image"].split(".")
    filename = input ("File name: ")
    savefile = filename + "." + name[1]
    # Check that the file does not exist
    if (os.path.isfile(savefile)):              
        print ("[ERROR] File {} already exist. Please verify".format(savefile))
        print ("[MSG] File not saved!")
    else:
        print ("Saving: ", savefile)
        cv.imwrite(savefile, image)
else:
    print ("[MSG] File not saved!")
    
cv.destroyAllWindows()