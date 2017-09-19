#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**************************************
*             COLOR MAP              *
*                                    *
*           Version: 1.4             *
**************************************

Press [s] to save the image
press any key to quit

# USAGE: 
    python color_map.py --image <imageFile> --color <colorMap>
    python color_map.py -i <imageFile> -c <colorMap>
***************************************
"""

# Import the necessary packages
import argparse
import cv2
import os.path

# Print routine header
print (__doc__)

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description = "Apply a color map to an image")

ap.add_argument("-i",
                "--image",
                required = True,
                help = "Path to the image")

ap.add_argument("-c",
                "--color",
                required = False,
                default = 0, 
                type = int,
                choices = range(0, 12),
                help ="Number of color map to apply (must be between 0 and 11)")

args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[ERROR] File {} does not exist. Please verify".format(args["image"]))
    exit(0)

print ("Applying color map No. {}".format(args["color"]))

# Load the image and convert it to grayscale
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(image, args["color"])
#im_color = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Show our images
cv2.imshow("Color Map", im_color)
key = cv2.waitKey(0) &0xFF

#save the file?
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
        cv2.imwrite(savefile, im_color)

cv2.destroyAllWindows()
  