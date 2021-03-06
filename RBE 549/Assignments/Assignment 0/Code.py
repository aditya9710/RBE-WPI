#### OpenCV on Python

### ->Problem 3

# Image

### ->Problem 4

import cv2 as cv
import numpy as np

# img = cv2.imread('logo.jpg')
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera.")
    exit()

while True:
    _, frame = cap.read()

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', grayFrame)
    if cv.waitKey(1) == ord('1'):
        break

cap.release()
cv.destroyAllWindows()
