# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:40:40 2016

@author: Stein
"""

import cv2
import argparse
import numpy as np

#Initialize the haars cascade 
faceCascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image, convert it to grayscale
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.3, 5)
print ("I found {} face(s)".format(len(faces)))

#define a black mask the size of the original image
mask = np.zeros(image.shape[:2], dtype = "uint8")

#loop throught the faces to apply the mask
padding = 10
for (x, y, w, h) in faces:
    cv2.rectangle(mask, (x-padding, y-padding), (x+w+padding , y+w+padding), 255, -1)
    masked = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("Mask Applied to Image", masked)
   
cv2.waitKey(0)
    


