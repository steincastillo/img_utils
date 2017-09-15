# -*- coding: utf-8 -*-
"""
**************************************
Created on Tue Oct 25 14:48:18 2016
Edited on 9/4/2017 1:07:16 PM
@author: Stein

**************************************
*            SHOW IMAGE              *
*            MATPLOTLIB              *
*            Version 1.0             *
**************************************

Usage:  python show_plt.py --image <imageFile>
        python show_plt.py -i <imageFile>
***************************************
"""

# Import libraries
import argparse
import os.path
import cv2 as cv
from matplotlib import pyplot as plt

# Define functions
def show_image(img):
    _,_,c = img.shape
    if c >= 3:    
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)  # Convert the image to RGB format
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()

# Calculate the mean brightness of the image
def mean_brigh(img):
    _,_,c = img.shape
    if c>= 3:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert image to grayscale
    return (cv.mean(img))


# Main loop
if __name__=="__main__":
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
    means = mean_brigh(image)

    # Display image properties
    print ("Image properties:")
    print ("-----------------")
    print ("* File: {}".format(args["image"]))
    print ("* Witdh: {}".format (w))
    print ("* Height: {}".format(h))
    print ("* Channels: {}".format(c))
    print ("* Pixels: {:.1f} M".format(size/1e6))
    print ("* File type: {}".format(imgtype))
    print ("* Mean brightness: {}".format(int(means[0])))
    print ("-----------------")
    print ("\n")

    # Display the image
    show_image(image)
