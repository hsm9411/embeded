from gpiozero import LED, Button, Buzzer
import random
import time

# 전역 변수로 score 선언
score = 0

# 부저, LED, 버튼 초기화
bz = Buzzer(12)
led_R = LED(5)
btn_R = Button(26, pull_up=True, bounce_time=0.05)
led_G = LED(27)
btn_G = Button(23, pull_up=True, bounce_time=0.05)
led_B = LED(17)
btn_B = Button(24, pull_up=True, bounce_time=0.05)

# R 매치 확인 함수 (LED가 켜져 있으면 점수 증가 및 부저 울림)
def is_R_match():
    global score  # 전역 변수 score 수정
    if led_R.is_lit or led_G.is_lit or led_B.is_lit:  # LED가 켜져 있으면
        score += 1  # 점수 1 증가
        print(f"점수: {score}")  # 점수 출력
        bz.on()
        time.sleep(0.2)
        bz.off()

# 버튼이 눌리면 is_R_match() 함수 실행
btn_R.when_pressed = is_R_match

# 무한 루프에서 LED 깜빡임과 랜덤 대기 시간 관리
while True:
    led_R.on()
    time.sleep(0.5)
    led_R.off()
    rTime = random.uniform(0.0, 4.0)  # 랜덤 시간 설정 (0.5초 ~ 4초 사이)
    time.sleep(rTime)  # 설정한 시간만큼 대기
