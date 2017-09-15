# -*- coding: utf-8 -*-
"""
**************************************
Created on Tue Oct 25 14:48:18 2016
Edited on 9/4/2017 1:07:16 PM
@author: Stein

**************************************
*            SHOW IMAGE              *
*                                    *
*            Version 1.7             *
**************************************

Usage:  python show_image.py --image <imageFile>
        python show_image.py -i <imageFile>
***************************************
"""

# Import libraries
import argparse
import os.path
import cv2 as cv
from matplotlib import pyplot as plt

# Print routine header
print (__doc__)

# Parse the arguments
ap = argparse.ArgumentParser(description="Display a picture on the screen")

ap.add_argument("-i",
                "--image",
                required=True,
                help ="Path to the image")

args = vars(ap.parse_args())

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[ERROR] File {} does not exist. Please verify.".format(args["image"]))
    exit(0)

image = cv.imread(args["image"])
(h, w, c) = image.shape
size = image.size
imgtype = image.dtype
image1 = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Convert image to grayscale
means = cv.mean(image1)

print ("Image properties:")
print ("-----------------")
print ("* File: {}".format(args["image"]))
print ("* Witdh: {}".format (w))
print ("* Height: {}".format(h))
print ("* Channels: {}".format(c))
print ("* Pixels: {:.2f} M".format(size/1e6))
print ("* File type: {}".format(imgtype))
print ("* Mean brightness: {}".format(int(means[0])))
print ("-----------------")
print ("\n")

image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
plt.imshow(image)
plt.xticks([]), plt.yticks([])
plt.show()
