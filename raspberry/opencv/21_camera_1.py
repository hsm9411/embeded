import numpy as np
import cv2
# Read from the first camera device
cap = cv2.VideoCapture(0)

w = 640#1280
h = 480#720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

# 원본 비디오의 프레임 속도(FPS)와 프레임 크기(가로, 세로) 얻기
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (width, height)

#out = cv2.VideoWriter(video_name,fourcc, fps, (w, h))

output_video_path = 'output_video.mp4' # 저장할 비디오 파일 이름
fourcc_code = cv2.VideoWriter_fourcc(*'mp4v') # 비디오 코덱 설정 (MP4용)

out = None  # 녹화 시작 시점에 VideoWriter 객체가 생성될 것임
is_recording = False

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    display_frame = frame.copy() # 원본 프레임 복사하여 텍스트 오버레이
    
    if is_recording:
        # 녹화 중임을 시각적으로 표시
        cv2.putText(display_frame, "REC", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.circle(display_frame, (30, 45), 10, (0, 0, 255), -1) # 빨간색 점    

    # Display
    cv2.imshow("Camera", frame)
    
    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    
    if key == ord('r'):
        if not is_recording:
            # VideoWriter 객체 생성
            out = cv2.VideoWriter(output_video_path, fourcc_code, fps, frame_size)
            if not out.isOpened():
                print(f"Error: Could not create video writer for {output_video_path}")
                # VideoWriter 생성 실패 시 is_recording을 False로 유지
            else:
                is_recording = True
                print(f"Recording started to {output_video_path}...")
        else:
            print("Recording is already in progress.")

    # 's' 키를 눌렀을 때 녹화 중지 및 저장
    elif key == ord('s'):
        if is_recording:
            is_recording = False
            if out is not None:
                out.release() # VideoWriter 객체 해제 (파일 저장 완료)
                out = None
                print(f"Recording stopped. Video saved to {output_video_path}")
            else:
                print("Error: VideoWriter object is None, but was recording. This shouldn't happen.")
        else:
            print("Not currently recording.")
    elif key & 0xFF == ord('q'):
        print("Exiting application.")
        break
    
    # 녹화 중일 때만 프레임을 비디오 파일에 쓰기
    if is_recording and out is not None:
        out.write(frame)

   
cap.release()

cv2.destroyAllWindows()