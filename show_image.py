# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:48:18 2016

@author: Stein
"""

import argparse
import cv2 as cv
from matplotlib import pyplot as plt

print("\n")
print("**************************************")
print("*             SHOW IMAGE             *")
print("*                                    *")
print("*           Version: 1.5             *")
print("**************************************")
print("\n")

ap = argparse.ArgumentParser(description="Display a picture on the screen")
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
(h, w, c) = image.shape
size = image.size
imgtype = image.dtype
image1 = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
means = cv.mean(image1)

print ("Image properties:")
print (" *File: ", args["image"])
print (" *Witdh: ", w)
print (" *Height: ", h)
print (" *Channels: ", c)
print (" *Pixels: ", size)
print (" *File type: ", imgtype)
print (" *Mean brightness: ", int(means[0]))
print ("\n")
print ("Press any key to close")
cv.namedWindow(str(args["image"]), cv.WINDOW_NORMAL)
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
    
cv.waitKey(0)