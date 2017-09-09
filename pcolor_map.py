#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/8/2017 4:38:02 PM

@author: Stein

*****************************************
*           Variable Color Map          *
*                       V1.0            *
*****************************************

usage:
    python pcolor_map.py -i <imageFile>
    python pcolor_map.py --image <imageFile>

press <ESC> to exit
press <s> to save
"""

# Import libraries
import cv2 as cv
import os.path
import argparse

# Define functions
def nothing(x):     # Dummy function for createTrackbar call
    pass

# Define variables
cm = 0
lcm = 0

# Main loop

print (__doc__)

ap = argparse.ArgumentParser(description="Variable Color Map")

ap.add_argument("-i",
                "--image", 
                required=True, 
                help ="Path to the image")

args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

# Read the image and apply initial color map
image_orginal = cv.imread(args["image"])
image_gray = cv.cvtColor(image_orginal, cv.COLOR_BGR2GRAY)
im_color = cv.applyColorMap(image_gray, cm)

# Create the image window
cv.namedWindow(args["image"])
cv.namedWindow("Color Map")

# Create trackbar
cv.createTrackbar("Color Map", "Color Map", 0, 11, nothing)

while True:
    cv.imshow(args["image"], image_orginal)
    cv.imshow("Color Map", im_color)

    k = cv.waitKey(1) & 0xFF

    if k == 27:     # press <ESC> to quit
        break

    # Save the file?
    if k == ord("s"):
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
            cv.imwrite(savefile, im_color)

    cm = cv.getTrackbarPos("Color Map", "Color Map")
    if cm!=lcm:
        lcm = cm
        print ("Color Map: {}".format(cm))
        im_color = cv.applyColorMap(image_gray, cm)
        
cv.destroyAllWindows()

