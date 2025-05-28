import numpy as np
import cv2
# Read from the recorded video file
cap = cv2.VideoCapture("ronaldinho.mp4")
# ??? ??? ????? ???? while ? ??

frame_count = 0 # 저장될 프레임 파일의 이름을 위한 카운터

while(cap.isOpened() ):
# ? ???? ???
    ret, frame = cap.read()
    if ret is False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
        if ret is False:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
    frame_count += 1
# Display
    cv2.imshow("Frame", frame)
# 1 ms ?? ???? ? ??? ?? 'q' ?? ? ??
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
# if enter c then capture frame which is playing now
    elif key & 0xFF == ord('c'):
        # 파일 이름 지정 (예: frame_0001.jpg, frame_0002.jpg)
        save_path = f"saved_frame_{frame_count:04d}.jpg"
        
        # cv2.imwrite()를 사용하여 프레임 저장
        # frame: 저장할 이미지 데이터 (NumPy 배열)
        # save_path: 저장할 파일 경로 및 이름
        success = cv2.imwrite(save_path, frame)
        if success:
            print(f"Frame saved successfully as {save_path}")
        else:
            print(f"Error: Could not save frame to {save_path}")
    
cap.release()
cv2.destroyAllWindows()