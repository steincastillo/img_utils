#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:09:05 2016

@author: Stein
"""

# this routine finds the brightest and darkest spots in an image
# a radius has to be provided and must be and odd number

# Import  libraries
import cv2
import argparse
import os.path

print("\n")
print("**************************************")
print("*           BRIGHT SPOT              *")
print("*                                    *")
print("*           Version: 1.0             *")
print("**************************************")
print("\n")
print ("Press [s] to save the image")
print ("press any key to quit")

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", 
                "--image", 
                required = True,
                help = "Path to the image")

ap.add_argument("-r",
                "--radius", 
                type= int,
                required = True,
                help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

# Verify that the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify.".format(args["image"]))
    exit(0)

# Load the image, convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply gaussian blur to the image
gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)

#find the brightest and darkest spot in the image
(minVal, Maxval, minLoc, maxLoc) = cv2.minMaxLoc(gray)

#Draw a circle around the brightest spot
cv2.circle(image, maxLoc, args["radius"], (255,0,0), 2)
cv2.putText(image, "+", ((maxLoc[0]-5), maxLoc[1]-(args["radius"]+5)),
             cv2.FONT_HERSHEY_SIMPLEX, 0.50, (255,0,0), 2)

#Draw a circle around the darkest spot
cv2.circle(image, minLoc, args["radius"], (0,0,255), 2)
cv2.putText(image, "-", ((minLoc[0]-5), minLoc[1]-(args["radius"]+5)),
             cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0,0,255), 2)

cv2.imshow("Bright", image)
key = cv2.waitKey(0) &0xFF

#save the file?
if key == ord("s"):
    #construct new file name
    filename = args["image"]
    pos = filename.find(".", len(filename)-5)
    name=filename[0:pos]
    extension = filename[pos:]
    savefile = name+"_bright"+"_R"+str(args["radius"])+extension
    print ("Saving: ", savefile)
    cv2.imwrite(savefile, image)