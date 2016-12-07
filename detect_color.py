# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:30:15 2016

@author: Stein
"""

#import libraries
import numpy as np
import argparse
import cv2
    
#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help ="path to the dataset of images")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [
        ([17, 15, 100], [50, 56, 200]),
        ([86, 31, 4], [220, 88, 50]),
        ([25, 146, 190], [62, 174, 250]),
        ([103, 86, 65], [145, 133, 128])
        ]

for (lower, upper) in boundaries:
    #create NumPy arrays from boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    
    #find the colors within the specified boundaries and apply 
    #the mask
    
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    
    #show de images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)