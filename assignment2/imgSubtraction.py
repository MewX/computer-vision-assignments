import numpy as np
import cv2
import sys

# argument number detection
if len(sys.argv) == 1:
    print("Usage: python3 {} image1 image2".format(sys.argv[0]))
    exit(0)

print(sys.argv)
image1 = cv2.imread(sys.argv[1])
image2 = cv2.imread(sys.argv[2])
# image3 = image1 - image2

def diff(img,img1): # returns just the difference of the two images
  return cv2.absdiff(img,img1)
  
def diff_remove_bg(img0,img,img1): # removes the background but requires three images 
  d1 = diff(img0,img)
  d2 = diff(img,img1)
  return cv2.bitwise_and(d1,d2)

# imgray = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 
# cv2.drawContours(image2, contours, -1, (0,255,0), 1)
# cv2.imwrite("c:\\see_this.jpg", image2)

cv2.imwrite("out/out3.jpg", diff(image2, image1))
