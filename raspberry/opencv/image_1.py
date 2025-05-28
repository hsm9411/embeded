import cv2
import numpy as np

img = cv2.imread("res/images.jpeg")

cv2.namedWindow("image", cv2.WINDOW_NORMAL )

print(img.shape)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.imwrite("output.png", img)

cv2.destroyALLWindows()