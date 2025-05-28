from gpiozero import LED, Button, Buzzer
import random
import time

# 전역 변수로 score 선언
score = 0

# 부저, LED, 버튼 초기화
bz = Buzzer(6)
led_R = LED(5)
btn_R = Button(26, pull_up=True, bounce_time=0.05)

# R 매치 확인 함수 (LED가 켜져 있으면 점수 증가 및 부저 울림)
def is_R_match():
    global score  # 전역 변수 score 수정
    if led_R.is_lit:  # LED가 켜져 있으면
        score += 1  # 점수 1 증가
        print(f"점수: {score}")  # 점수 출력
        bz.beep(on_time=0.2, off_time=0)  # 부저 울리기

# 버튼이 눌리면 is_R_match() 함수 실행
btn_R.when_pressed = is_R_match

# 무한 루프에서 LED 깜빡임과 랜덤 대기 시간 관리
while True:
    led_R.blink(on_time=0.5, off_time=0.5)  # LED 깜빡이기 (0.5초 간격)
    onTime = random.uniform(0.5, 5.0)  # 랜덤 시간 설정 (0.5초 ~ 5초 사이)
    time.sleep(onTime)  # 설정한 시간만큼 대기
