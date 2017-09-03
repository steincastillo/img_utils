#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:20:44 2017
@author: Stein

*****************************************
*            Add Text To Image          *
*                 V1.0                  *
*****************************************

usage: 
    python addtext.py -i <imageFile> -c <textColor>
    python addtext.py --image <imageFile> --color <textColor>

Color options:
    white, black, red, green, blue

"""

# Import libraries
import cv2 as cv
import argparse
import os.path

# Define text constants
WHITE = (255,255,255)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
FONT = cv.FONT_HERSHEY_SIMPLEX
LINE = cv.LINE_AA

# Print header
print (__doc__)

# Parse the arguments
ap = argparse.ArgumentParser(description="Add text to an image")

ap.add_argument("-i", "--image", required=True, help ="Path to the image")

ap.add_argument("-c", "--color", required=False, default ="white", 
                help ="Text color")

args = vars(ap.parse_args())

# Set text color
color = args["color"].lower()
if color == "black":
    txtcolor = BLACK
elif color == "blue":
    txtcolor = BLUE
elif color == "green":
    txtcolor = GREEN
elif color == "red":
    txtcolor = RED
else:
    txtcolor = WHITE

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

# Open the image file
image = cv.imread(args["image"])

# Get the input from the user 
line1 = input ("Line 1: ")
line2 = input ("Line 2: ")
line3 = input ("Line 3: ")

# Get image dimensions
height, width, _ = image.shape

# Calculate position for the text lines
pl3 = height - 10
pl2 = height - 25
pl1 = height - 40

# Add text lines to the image
cv.putText(image, line1, (10, pl1), FONT, 0.5, txtcolor, 1, LINE)
cv.putText(image, line2, (10, pl2), FONT, 0.5, txtcolor, 1, LINE)
cv.putText(image, line3, (10, pl3), FONT, 0.5, txtcolor, 1, LINE)

print ("Press [s] to save")
print ("Press any key to quit")

# Present original image
cv.namedWindow(args["image"], cv.WINDOW_NORMAL)
cv.imshow(args["image"], image)

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
        print ("[MSG] File not saved!")
        exit(0)
    print ("Saving: ", savefile)
    cv.imwrite(savefile, image)
else:
    print ("[MSG] File not saved!")

cv.destroyAllWindows()
