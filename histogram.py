# -*- coding: utf-8 -*-

"""
Program: histogram.py
Date created: 04-Oct-2016
Author: Stein Castillo
Version 1.5
Copyright 2016 Stein Castillo <stein_castillo@yahoo.com>

USAGE: python3 histogram.py -f [picture.file]
"""

#############
# Libraries #
#############
import cv2 as cv
from matplotlib import pyplot as plt
import argparse
import warnings

####################
#    Settings     #
####################
#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the picture file")
args = vars(ap.parse_args())
warnings.filterwarnings("ignore")
#conf = json.load(open(args["file"]))
FILE = args["image"]

print("\n")
print("**************************************")
print("*             HISTOGRAM              *")
print("*                                    *")
print("*           Version: 1.5             *")
print("**************************************")
print("\n")

img = cv.imread(FILE)
img1 = cv.imread(FILE, 0)
print ("Image properties:")
print (" * File: " + FILE)
print (" * Shape: " + str(img.shape))
print (" * Size: " + str(img.size))
print (" * Type: " + str(img.dtype))

if len(img.shape)<3:  #grayscale image
    plt.hist(img.ravel(), 256,[0,256])
    plt.title("Histogram fro grey scale picture")
    plt.show()
else:                   #color image
    color = ("b", "g", "r")
    for i,col in enumerate(color):
        histr = cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color = col)
        plt.xlim([0,256])
    #plt.hist(img1.ravel(), 256,[0,256])
    plt.title(FILE)
    plt.show()
    
print ("Done!")
