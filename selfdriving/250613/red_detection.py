
import cv2
import numpy as np

def nothing(x):
    pass

# 이미지 읽기
image = cv2.imread('sample.png')  # 여기에 원하는 이미지 파일 경로 입력
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# 윈도우 및 트랙바 생성
cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)

cv2.createTrackbar("L min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("A min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("A max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("B min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("B max", "Trackbars", 255, 255, nothing)


while True:
    # 트랙바 값 읽기
    l_min = cv2.getTrackbarPos("L min", "Trackbars")
    l_max = cv2.getTrackbarPos("L max", "Trackbars")
    a_min = cv2.getTrackbarPos("A min", "Trackbars")
    a_max = cv2.getTrackbarPos("A max", "Trackbars")
    b_min = cv2.getTrackbarPos("B min", "Trackbars")
    b_max = cv2.getTrackbarPos("B max", "Trackbars")

    lower = np.array([l_min, a_min, b_min])
    upper = np.array([l_max, a_max, b_max])

    # 마스크 생성
    mask = cv2.inRange(lab_image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    # 이미지에 텍스트로 표시

    # 살아남은 픽셀 수 계산
    pixel_count = cv2.countNonZero(mask)

    # 콘솔 출력
    print(f"Matched pixels: {pixel_count}")

    # 시각화
    cv2.imshow("Original", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered Result", result)
    display_result = result.copy()
    cv2.putText(display_result, f"Pixels: {pixel_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Filtered Result", display_result)
    key = cv2.waitKey(1)
    if key == 27:  # ESC 키
        break

cv2.destroyAllWindows()
