# -*- coding: utf-8 -*-
# USAGE: python color_map.py --image [image] --color [colormap]

# Import the necessary packages
import argparse
import cv2
import os.path

print("\n")
print("**************************************")
print("*             COLOR MAP              *")
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
ap.add_argument("-c", "--color", required = True, type = int,
                help ="Color map to apply (0-11)")
args = vars(ap.parse_args())

if not(os.path.isfile(args["image"])):              # Verify if the file exists
    print ("[Error] File {} does not exist. Please verify\n".format(args["image"]))
    exit(0)

print ("Applying color map No. {}".format(args["color"]))

# Load the image and convert it to grayscale
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(image, args["color"])
#im_color = cv2.applyColorMap(image, cv2.COLORMAP_JET)

# Show our images -- notice how the constrast of the second
# image has been stretched
cv2.imshow("Color Map", im_color)
key = cv2.waitKey(0) &0xFF

#save the file?
if key == ord("s"):
    #construct new file name
    filename = args["image"]
    pos = filename.find(".", len(filename)-5)
    name=filename[0:pos]
    extension = filename[pos:]
    savefile = name+"_color"+str(args["color"])+extension
    print ("Saving: ", savefile)
    cv2.imwrite(savefile, im_color)
else:
    print ("[MSG] File not saved!")
  