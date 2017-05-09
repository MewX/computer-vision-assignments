import numpy as np
import cv2
import sys

# command line input: python3 xxx.py file1 (file2, ..., fileN)
face_cascade = cv2.CascadeClassifier('data/hello/haarcascade_frontalface_default.xml')

# argument number detection
if len(sys.argv) == 1:
    print("Usage: python3 {} fileName1 [fileName2 ... fileName3]".format(sys.argv[0]))
    exit(0)

# for i in range
picNum = len(sys.argv) - 1
for i in range(1, 1 + picNum):
    filePath = sys.argv[i].strip()
    fileName = filePath[max(filePath.rfind('/'), filePath.rfind('\\')) + 1:]

    print("Now processing \"{}\" ...".format(fileName))
    img = cv2.imread(filePath)
    print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    print("done")

    cv2.imwrite("out/" + fileName, img)
    cv2.destroyAllWindows()
