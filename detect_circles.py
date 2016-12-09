# -*- coding: utf-8 -*-
# USAGE
# python equalize.py --image [image]

# Import the necessary packages
import numpy as np
import argparse
import cv2
import mahotas

print("\n")
print("**************************************")
print("*        Circle Detection            *")
print("*                                    *")
print("*           Version: 1.0             *")
print("**************************************")
print("\n")
print ("Press [s] to save the image")
print ("press any key to quit")

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 5)

#Threshold the image
thresh = blurred.copy()
T = mahotas.thresholding.otsu(thresh)
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)



#detect circles
#circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 120, param1=100,
#			param2=30, minRadius=0, maxRadius=0)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.6, 100)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
	#Draw the outer circle
	cv2.circle(image, (i[0], i[1]), i[2], (0,255,0), 2)
	#draw center of the circle
	cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 3)

cv2.imshow("Otsu", thresh)
cv2.imshow("Hough Circles", image)

key = cv2.waitKey(0) &0xFF

#Save the file?
if key == ord("s"):
    #construct new file name
    filename = args["image"]
    pos = filename.find(".", len(filename)-5)
    name=filename[0:pos]
    extension = filename[pos:]
    savefile = name+"_eq"+extension
    print ("Saving: ", savefile)
    cv2.imwrite(savefile, eq)

cv2.destroyAllWindows()
  