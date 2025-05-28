import cv2
import numpy as np

points = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point {len(points)}: {x}, {y}")

def warp_image(img, pts):
    w, h = 500, 300 # 정사각형으로 변환
    dst_pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)
    # 입력된 점들을 정렬
    sorted_pts = sort_points(pts)
    matrix = cv2.getPerspectiveTransform(np.array(sorted_pts, dtype=np.float32), dst_pts)
    return cv2.warpPerspective(img, matrix, (w, h))

def sort_points(pts):
    """
    4개의 점을 left_top, right_top, right_bottom, left_bottom 순서로 정렬
    보다 견고한 방법으로 수정
    """
    pts_np = np.array(pts, dtype=np.float32)

    # 1. x 좌표를 기준으로 정렬
    # pts_np를 복사하여 정렬에 사용 (원본 변경 방지)
    sorted_by_x = pts_np[np.argsort(pts_np[:, 0])]

    # 2. 왼쪽 두 점과 오른쪽 두 점 분리
    left_most = sorted_by_x[:2]
    right_most = sorted_by_x[2:]

    # 3. 각 그룹에서 y 좌표 기준으로 정렬하여 최종 순서 결정
    # 왼쪽 두 점 중 y가 작은 것이 left_top, 큰 것이 left_bottom
    left_top = left_most[np.argmin(left_most[:, 1])]
    left_bottom = left_most[np.argmax(left_most[:, 1])]

    # 오른쪽 두 점 중 y가 작은 것이 right_top, 큰 것이 right_bottom
    right_top = right_most[np.argmin(right_most[:, 1])]
    right_bottom = right_most[np.argmax(right_most[:, 1])]

    # 순서대로 정렬: left_top, right_top, right_bottom, left_bottom
    sorted_pts = np.array([left_top, right_top, right_bottom, left_bottom], dtype=np.float32)
    return sorted_pts

img = cv2.imread('res/card2.jpg')
clone = img.copy()
cv2.namedWindow("Select 4 Points")
cv2.setMouseCallback("Select 4 Points", mouse_callback)

while True:
    temp = clone.copy()
    for pt in points:
        cv2.circle(temp, pt, 5, (0, 255, 0), -1)
    cv2.imshow("Select 4 Points", temp)

    key = cv2.waitKey(1)
    if key == 27: # ESC
        break
    if len(points) == 4:
        warped = warp_image(clone, points)
        cv2.imshow("Warped", warped)
        
cv2.destroyAllWindows()