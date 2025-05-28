import cv2
# 이미지 읽기 – 파일과 경로는 각자 맞게 수정해야 함
img = cv2.imread("res/card2.jpg")
# 이미지가 잘 로드 됐는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()
# 이미지 보여주기
cv2.imshow("Loaded Image", img)
# 키 입력 대기 (무한 대기)
key = cv2.waitKey(0)
# 's' 키를 누르면 이미지 저장
if key == ord('s'): # ord 는 ASCII(아스키) 코드 값을 정수로 반환하는 Python 내장 함수
    cv2.imwrite("saved_image.jpg", img)
    print("Saved as a saved_image.jpg file!!")
    
cv2.destroyAllWindows()