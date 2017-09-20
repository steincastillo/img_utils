#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:15:54 2017

@author: Stein Castillo

**************************************
*          SHOW EXIF DATA            *
*            Version 1.3             *
**************************************

Usage:  python show_exif.py --image <imageFile>
        python show_exif.py -i <imageFile>
***************************************
"""

# Import libraries
import argparse
import os.path
import cv2 as cv
import pprint
from matplotlib import pyplot as plt
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Define functions
def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data

def _get_if_exist(data, key):
    if key in data:
        return data[key]
    
    return None

def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return lat, lon

def img_type(img):
    import imghdr
    return (imghdr.what(img))

def show_image(img):
#    _,_,c = img.shape
#    if c >= 3:    
#        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)  # Convert the image to RGB format
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()

    
# Main loop
if __name__== "__main__":
    # Print routine header
    print (__doc__)

    # Parse the arguments
    ap = argparse.ArgumentParser(description="Display image EXIF data",
                                 epilog = "Uses matplotlib to display the image")

    ap.add_argument("-i",
                    "--image",
                    required=True,
                    help ="Path to the image")
    
    ap.add_argument("-r",
                    "--raw",
                    required=False,
                    default = "True",
                    choices = ["True", "False", "true", "false"],
                    help ="EXIF raw data dump?")
    
    ap.add_argument("-d",
                    "--disp",
                    required=False,
                    default = "False",
                    choices = ["True", "False", "true", "false"],
                    help ="Display the image?")

    args = vars(ap.parse_args())

    # Verify that the file exists
    if not(os.path.isfile(args["image"])):              
        print ("[ERROR] File {} does not exist. Please verify.".format(args["image"]))
        exit(0)
        
    # Open the image file
    image = Image.open(args["image"])
    
    exif_data = get_exif_data(image)
    
    if exif_data=={}:
        print ("[INFO] image: {} has EXIF data... Exiting.".format(args["image"]))
        exit(0)
        
    # Delete unused attributes from the exif data dictionary
    if (_get_if_exist(exif_data, "MakerNote"))!=None:
        del exif_data["MakerNote"]
        
    if _get_if_exist(exif_data, "PrintImageMatching")!=None:
        del exif_data["PrintImageMatching"]
        
    # Get image coordinates
    lat, lon = get_lat_lon(exif_data)
    if lat == None: lat = 0
    if lon == None: lon = 0
    # Get image resolution
    img_res = _get_if_exist(exif_data,"XResolution")
    if img_res != None: img_res = img_res[0]
    
    # Print the EXIF data
    if args["raw"].lower() == "true":
        print ("Image raw EXIF data dump")
        print ("************************")
        pp = pprint.PrettyPrinter()
        pp.pprint(exif_data)
        print ("Coordinates:")
        print ("Latitude: {:.3f} degrees".format(lat))
        print ("Longitue: {:.3f} degrees".format(lon))
    else:
        print ("Image Properties:")
        print ("*****************")
        print ("* File: {}".format(args["image"]))
        print ("* Date: {}".format(_get_if_exist(exif_data, "DateTime")))
        print ("* Author: {}".format(_get_if_exist(exif_data, "Artist")))
        print ("* Height: {} px".format(_get_if_exist(exif_data, "ExifImageHeight")))
        print ("* Width: {} px".format(_get_if_exist(exif_data, "ExifImageWidth")))
        print ("* Resolution: {} ppi".format(img_res))
        print ("* Image type: {}".format(img_type(args["image"])))
        print ("* ISO speed rating: {}".format(_get_if_exist(exif_data, "ISOSpeedRatings")))
        print ("* Camera make: {}".format(_get_if_exist(exif_data, "Make")))
        print ("* Camera model: {}".format(_get_if_exist(exif_data, "Model")))
        print ("* Latitude: {:.3f} degrees".format(lat))
        print ("* Longitude: {:.3f} degrees".format(lon))
        
    # Display the image?
    if args["disp"].lower() == "true":
        show_image(image)

    
