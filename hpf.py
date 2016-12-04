
import cv2
import numpy as np 
from scipy import ndimage
import argparse

print("\n")
print("**************************************")
print("*         High Pass Filter           *")
print("*                                    *")
print("*           Version: 1.0             *")
print("**************************************")
print("\n")

kernel_3x3 = np.array([[-1, -1, -1],
					[-1, 8, -1],
					[-1, -1, -1]])

kernel_5x5 =  np.array([[-1, -1, -1, -1, -1],
						[-1,  1,  2,  1, -1],
						[-1,  2,  4,  2, -1],
						[-1,  1,  2,  1, -1],
						[-1, -1, -1, -1, -1]])

ap = argparse.ArgumentParser(description="Apply high pass filter to an image")
ap.add_argument("-i", "--image", required=True, help ="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], 0)

k3 = ndimage.convolve(image, kernel_3x3)
k5 = ndimage.convolve(image, kernel_5x5)

blurred = cv2.GaussianBlur(image, (11,11), 0)
g_hpf = image - blurred

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()
