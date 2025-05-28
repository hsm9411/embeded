import cv2
# 이미지 로드
img = cv2.imread("res/card4.jpeg")
# 이미지 로드 실패 시 종료
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()
# 1. 이미지 크기 확대 (2배)
scaled_up = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
# 2. 이미지 크기 축소 (1/2배)
scaled_down = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# 3. 좌우 대칭 (flipCode=1)
flipped = cv2.flip(img, 1)
# 4. 90도 회전 (시계 방향)
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 결과 이미지 보기
cv2.imshow("Original", img)
cv2.imshow("Scaled Up x2", scaled_up)
cv2.imshow("Scaled Down x0.5", scaled_down)
cv2.imshow("Flipped (Left-Right)", flipped)
cv2.imshow("Rotated 90 Clockwise", rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()