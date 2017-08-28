
# Import libraries
import cv2 as cv
import numpy as np
import os.path
import argparse

def nothing(x):     # Dummy function for createTrackbar call
    pass

ap = argparse.ArgumentParser(description="Find image contours")
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

image_orginal = cv.imread(args["image"])
image = cv.cvtColor(image_orginal, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(image, (5, 5), 0)
blurred1 = blurred


# Create the image window
cv.namedWindow("image")

# Create trackbar
cv.createTrackbar("THR", "image", 3, 255, nothing)
th = 3
lth = 3

while True:
    cv.imshow("image", blurred)
    k = cv.waitKey(1) & 0xFF
    if k == 27:     # press <ESC> to quit
        break

    th = cv.getTrackbarPos("THR", "image")
    if th!=lth:
        lth = th
        print (th)
        (t, blurred) = cv.threshold(blurred1, th, 255, cv.THRESH_BINARY)


cv.destroyAllWindows()

