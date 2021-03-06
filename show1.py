# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:48:18 2016
@author: Stein

**************************************
*            SHOW IMAGE              *
*                                    *
*            Version 1.7             *
**************************************

Usage:  python show_image.py --image <imageFile>
        python show_image.py -i <imageFile>
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
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
args = vars(ap.parse_args())

# Verify the file exists
if not(os.path.isfile(args["image"])):              
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
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
print ("Press any key to close")
cv.namedWindow(str(args["image"]), cv.WINDOW_NORMAL)
cv.moveWindow(str(args["image"]), 100, 10)
cv.imshow(str(args["image"]), image)

if len(image.shape)<3:  #grayscale image
    plt.hist(image.ravel(), 256,[0,256])
    plt.title("Histogram from grey scale picture")
    plt.show()
else:                   #color image
    color = ("b", "g", "r")
    for i,col in enumerate(color):
        histr = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr, color = col)
        plt.xlim([0,256])
    plt.title(args["image"])
    plt.show()
    
key = cv.waitKey(0) &0xFF

cv.destroyAllWindows()

