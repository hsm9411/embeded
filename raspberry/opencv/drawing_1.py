import cv2
import numpy as np

# 1. 하얀색 스케치북 생성
height, width = 720, 1280
sketchbook = np.ones((height, width, 3), dtype=np.uint8) * 255  # 흰색 배경

# 2. 상태 변수
drawing = False
prev_point = None

# 3. 마우스 콜백 함수
def draw_black_line(event, x, y, flags, param):
    global drawing, prev_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(sketchbook, prev_point, (x, y), color=(0, 0, 0), thickness=2)
        prev_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_point = None

# 4. 윈도우 생성 및 콜백 등록
cv2.namedWindow("스케치북", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("스케치북", draw_black_line)

# 5. 메인 루프
while True:
    cv2.imshow("스케치북", sketchbook)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 누르면 종료
        break

cv2.destroyAllWindows()
