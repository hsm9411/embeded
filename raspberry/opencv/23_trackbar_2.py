import numpy as np
import cv2

cap = cv2.VideoCapture("ronaldinho.mp4")
topLeft = (50, 50)
bold = 0
# Callback function for the trackbar
def on_bold_trackbar(value):
    #print("Trackbar value:", value)
    global bold
    bold = value

cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Text
    cv2.putText(frame, "TEXT",topLeft, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 1 + bold)

    # Display
    cv2.imshow("Camera",frame)

cap.release()
cv2.destroyAllWindows()