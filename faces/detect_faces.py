# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:40:40 2016

Detect faces in an image using the Haars Cascade Method

@author: Stein
"""

import cv2
import argparse
import numpy as np

#Initialize the haars cascade 
faceCascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")	#Std face detector
head_shoulder = cv2.CascadeClassifier("./cascades/HS.xml")								#Head and Shoulder detector

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image, convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.3, 5)
top = head_shoulder.detectMultiScale(gray, 1.3, 5)
#profiles = profileCascade.detectMultiScale(gray, 1.3, 5)
print ("I found {} frontal face(s)".format(len(faces)))
print ("I found {} Head-Shoulder(s)".format(len(top)))

#if faces were found loop throught the faces to draw rectangules
if len(faces)>0:
	padding = 10
	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x-padding, y-padding), (x+w+padding , y+h+padding), 255, 2)

	for (x,y, w, h) in top:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    
	#Display the image with detected faces in rectangles
	cv2.imshow("Faces", image)   
	cv2.waitKey(0)
else:
	print ("no faces were found")
    


