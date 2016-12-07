# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:43:30 2016

@author: Stein
"""

#import libraries
import numpy as np
import argparse
import cv2
    
#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help ="path to the dataset of images")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], 0)
canny = cv2.Canny(image, 200, 300)
cv2.imshow("Canny", np.hstack([image, canny]))

key = cv2.waitKey(0) &0xFF

#Save the file?
if key == ord("s"):
    #construct new file name
    filename = args["image"]
    pos = filename.find(".", len(filename)-5)
    name=filename[0:pos]
    extension = filename[pos:]
    savefile = name+"_canny"+extension
    print ("Saving: ", savefile)
    cv2.imwrite(savefile, canny)

cv2.destroyAllWindows()
