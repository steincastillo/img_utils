# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:26:14 2016

@author: Stein
"""

#import numpy as np
import datetime
import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser(description="Display video feed on the screen")
ap.add_argument("-f", "--flip", required=False, help ="Flip the video feed")
args = vars(ap.parse_args())

print("\n")
print("**************************************")
print("*          Image Capture             *")
print("*                                    *")
print("*           Version: 1.2             *")
print("**************************************")
print("\n")

print ("[q] to quit")
print ("[c] to capture")

#instancinte the camera
camera = cv2.VideoCapture(0)

#Set camera resolution
camera.set(3, 1024)
camera.set(4, 768)

#set camera FPS
camera.set(5, 30)

#create window to display the video feed
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

while True:
    ret, frame = camera.read()
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #should the image be mirrowed?
    if args["flip"]:
        mirror = np.fliplr(frame).copy()
        cv2.imshow("Frame", mirror)
    else:
        cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key  == ord("q") or key == ord("Q"):
        print ("Exiting...")
        break
    
    if key == ord("c"):
        file = "image1.png"
        #Add date and time to the image
        ts = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 
        0.4, (0, 0, 255), 1)
        #Write image file
        cv2.imwrite(file, frame)
        print("Captured!")
    
camera.release()
cv2.destroyAllWindows()
