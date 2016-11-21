# -*- coding: utf-8 -*-
# USAGE
# python equalize.py --image [image]

# Import the necessary packages
import numpy as np
import argparse
import cv2

print("\n")
print("**************************************")
print("*        IMAGE EQUALIZATION          *")
print("*                                    *")
print("*           Version: 1.5             *")
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
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization to stretch the constrast
# of our image
eq = cv2.equalizeHist(image)

# Show our images -- notice how the constrast of the second
# image has been stretched
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
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


  