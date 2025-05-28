import cv2
import numpy as np

img = cv2.imread("res/images.jpeg")


cropped = img[50:450, 100:400]

resized = cv2.resize(cropped, (450,600))

cv2.imshow("origin", img)
cv2.imshow("cropped", cropped)
cv2.imshow("resized", resized)

cv2.waitKey(0)

cv2.destroyALLWindows()