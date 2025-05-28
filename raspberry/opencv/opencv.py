import cv2
import numpy as np
# 1. 720p 해상도의 빈 스케치북 (검정 바탕)
height, width = 720, 1280
sketchbook = np.zeros((height, width, 3), dtype=np.uint8) # 초기값은 모두 0, 즉 검정색
window_name = "스케치북" # 윈도우 이름 설정
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) # OpenCV 창 생성
# 1. 검정색으로 화면 보여주기
cv2.line(sketchbook, (1,1), (1200,700), (0,0,255), 1)
cv2.circle(sketchbook, (500,500), 200, (255,255,255), 20)
cv2.rectangle(sketchbook, (200,200), (400,400), (255,255,0), 10)
pts = np.array([[100, 100], [200, 300], [400, 200]], np.int32)
cv2.polylines(sketchbook, [pts], isClosed=True, color=(255, 255, 0), thickness=5)
cv2.imshow(window_name, sketchbook)

cv2.setWindowTitle(window_name, "검정색 스케치북")
cv2.waitKey(1000)
# 2. 흰색으로 화면 전체 칠하기
sketchbook[:] = (255, 255, 255) # BGR 순서
cv2.imshow(window_name, sketchbook)
cv2.setWindowTitle(window_name, "흰색 스케치북")
cv2.waitKey(1000) # 1초 대기
# 3. 빨간색으로 화면 전체 칠하기
sketchbook[:] = (0, 0, 255) # 빨간색 (OpenCV는 BGR)
cv2.imshow(window_name, sketchbook)
cv2.setWindowTitle(window_name, "빨간색 스케치북")
cv2.waitKey(1000)
# 4. 종료
cv2.destroyAllWindows()