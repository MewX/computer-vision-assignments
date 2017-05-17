import numpy as np
import cv2
import sys

# this file will combine all the images in out/yale with the width of 15 images.
# all images are: 320 x 243
# argument number detection
if len(sys.argv) == 1:
    print("Usage: python3 {} out/yale/*".format(sys.argv[0]))
    exit(0)

height = 15 * 243
width = 11 * 320
output = np.zeros((height, width, 3))

# for i in range
picNum = len(sys.argv) - 1
x = 0
y = 0
imgCount = 0;
for i in range(1, 1 + picNum):
    filePath = sys.argv[i].strip()
    fileName = filePath[max(filePath.rfind('/'), filePath.rfind('\\')) + 1:]

    print("Now processing \"{}\",".format(fileName))
    img = cv2.imread(filePath)
    h, w, d = img.shape
    print(y, x, d)
    output[y:y+h,x:x+w] = img
    x += w
    imgCount += 1
    if imgCount % 11 == 0:
        print("line break")
        y += h
        x = 0

cv2.imwrite("out/yaleall.jpg", output)
