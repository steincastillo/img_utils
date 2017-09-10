#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 10:40:17 2017

@author: Stein

*****************************************
*         Image Filter Utility          *
*                 V1.0                  *
*****************************************

Usage:
    python effect.py -i <imageFile> -f <filter>
    python coloreq.py --image <imageFile> --filter <filter>
    
filter options:
    sharpen: Sharpen the image
    gray: Convert to gray scale
*****************************************
"""

# Impoer libraries
import cv2 as cv
import numpy as np
import argparse
import os.path

# Display the header
print (__doc__)

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description = "Image filter utility")

ap.add_argument("-i",
                "--image",
                required = True,
                help = "Path to the image")

ap.add_argument("-f",
                "--filter",
                required = True,
                help = "Effect to apply to the image")

args = vars(ap.parse_args())

# Verify if the file exists
if not(os.path.isfile(args["image"])):              
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)
    
# Open the image
image = cv.imread(args["image"])

# Verify input image is a color image
height, width, channels = image.shape
#if channels >= 3 :
#    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

filter = args["filter"].lower()
action = False

# SHARPEN
if filter == "sharpen":
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    img_output = cv.filter2D(image, -1, kernel)
    action = True
 
# convert to grayscale
elif filter == "gray":
    if channels >= 3 :
        img_output = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        action = True
    else: 
        print ("[ERROR]: Image is not color. Please verify")
        
else:
    print ("[ERROR] Filter option invalid. Please verify")
    
# Present the results?
if action:
    cv.namedWindow(args["image"], cv.WINDOW_NORMAL)
    cv.namedWindow(filter.upper(), cv.WINDOW_NORMAL)
    cv.imshow(args["image"], image)
    cv.imshow(filter.upper(), img_output)
    
    key = cv.waitKey(0)
    
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
            cv.imwrite(savefile, img_output)
    
    cv.destroyAllWindows()
    
    
