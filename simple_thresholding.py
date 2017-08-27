# USAGE
# python simple_thresholding.py --image [image]

# Import the necessary packages
import numpy as np
import os.path 
import argparse
import cv2

print("\n")
print("**************************************")
print("*        SIMPLE   THRESHOLDING       *")
print("*                                    *")
print("*           Version: 1.0             *")
print("**************************************")
print("\n")
print ("press any key to quit")

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

# Load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

#Apply simple thresholding to the image
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

#Apply simple inverse thesholding to the image
(T, thresh_inv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)

#Apply the thresholded image as a mask to the original
cv2.imshow("Mask", cv2.bitwise_and(image, image, mask=thresh_inv))

cv2.imshow("Simple Threshold", thresh)
cv2.imshow("Inverse Threshold", thresh_inv)
cv2.waitKey(0)