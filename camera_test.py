# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:56:27 2016

@author: Stein
"""

import cv2 as cv

ramp_frames = 5

camera = cv.VideoCapture(0)

def get_image():
    retval, im = camera.read()
    return im
    
for i in range(ramp_frames):
    temp = get_image()

print ("Taking picture...")
camera_capture = get_image()
file = "image1.png"

camera.release()

cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", camera_capture)
cv.waitKey(0)
cv.destroyWindow("Image")

cv.imwrite(file, camera_capture)


