import cv2
import numpy as np
# 1. 720p 해상도의 빈 스케치북 (검정 바탕)
height, width = 720, 1280
sketchbook = np.zeros((height, width, 3), dtype=np.uint8) # 초기값은 모두 0, 즉 검정색
# 2. 직선 그리기 - 시작점 (100, 100) → 끝점 (400, 300), 색상은 초록색, 두께는 3픽셀
cv2.line(sketchbook, (100, 100), (400, 300), color=(0, 255, 0), thickness=3)
# 3. 원 그리기 - 중심점 (600, 150), 반지름 60, 색상은 빨간색, 두께는 5픽셀
cv2.circle(sketchbook, center=(600, 150), radius=60, color=(0, 0, 255), thickness=5)
# 4. 사각형 그리기 - 왼쪽 위 (800, 200) → 오른쪽 아래 (1100, 400), 색상은 파란색, 채워진 형태
cv2.rectangle(sketchbook, (800, 200), (1100, 400), color=(255, 0, 0), thickness=-1)
# 5. 다각형 그리기 (삼각형 예제) - 꼭짓점 좌표 리스트 정의
#pts = np.array([[500, 500], [700, 600], [600, 700]], np.int32)
#pts = pts.reshape((-1, 1, 2)) # OpenCV가 요구하는 형태로 reshape
#cv2.polylines(sketchbook, [pts], isClosed=True, color=(255, 255, 0), thickness=4)
# 6. 결과 출력
cv2.namedWindow("스케치북", cv2.WINDOW_NORMAL) # 크기 조절 가능한 창 생성
cv2.resizeWindow("스케치북", height, width) # 창 크기 강제 설정
cv2.imshow("스케치북", sketchbook)
cv2.waitKey(0) # 별도의 키 입력이 있을때까지 imshow 로 생성된 창을 열어둠
cv2.destroyAllWindows()