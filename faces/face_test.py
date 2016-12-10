# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:32:28 2016

@author: Stein
"""

import cv2
#import sys

#cascPath = sys.argv[1]
#faceCascade = cv.CascadeClassifier(cascPath)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#        gray,
#        scaleFactor=1.1,
#        minNeighbor=5,
#        minSize=(30, 30),
#        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
#        )
        
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        roi_color = frame[y:y+h, x:x+w]
        
    cv2.imshow("Video", frame)
    #cv2.imshow("Face", roi_color)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()