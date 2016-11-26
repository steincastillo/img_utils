# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:26:14 2016

@author: Stein
"""

#import numpy as np
import datetime
import cv2 as cv
import winsound


print("\n")
print("**************************************")
print("*          Image Capture             *")
print("*                                    *")
print("*           Version: 1.0             *")
print("**************************************")
print("\n")

print ("[q] to quit")
print ("[c] to capture")

#instancinte the camera
camera = cv.VideoCapture(0)

#Set camera resolution
camera.set(3, 1024)
camera.set(4, 768)

#set camera FPS
camera.set(5, 30)

while True:
    ret, frame = camera.read()
    
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Frame", frame)
    
    key = cv.waitKey(1) & 0xFF
    
    if key  == ord("q"):
        print ("Exiting...")
        winsound.PlaySound("Bye_Bye.wav", winsound.SND_FILENAME)
        break
    
    if key == ord("c"):
        file = "image1.png"
        #Add date and time to the image
        ts = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
        cv.putText(frame, ts, (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 
        0.4, (0, 0, 255), 1)
        #Write image file
        cv.imwrite(file, frame)
        winsound.PlaySound("shutter-click-01.wav", winsound.SND_FILENAME)
        print("Captured!")
    
camera.release()
cv.destroyAllWindows()
