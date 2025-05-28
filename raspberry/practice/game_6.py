from gpiozero import LED, Button, Buzzer, TonalBuzzer
from gpiozero.tones import Tone
import random
import time
import threading

# 전역 변수로 score 선언
score = 0
led_on_count = 0  # 불이 켜진 횟수를 세는 변수

# 도레미파솔 음계
notes = ["C4", "D4", "E4", "F4", "G4"]

def play_scale(buzzer, notes, duration=1):
    """
    주어진 음계(notes)를 1초 간격으로 재생하는 함수.
    
    :param buzzer: TonalBuzzer 객체
    :param notes: 음계 리스트 (예: ["C4", "D4", "E4", "F4", "G4"])
    :param duration: 각 음을 재생할 시간 (기본값은 1초)
    """
    for note in notes:
        buzzer.play(Tone(note))  # 음을 재생
        sleep(duration)  # 지정된 시간만큼 대기
        buzzer.stop()  # 부저 끄기

# 부저, LED, 버튼 초기화
bz = TonalBuzzer(12)

led_1 = LED(5)
led_2 = LED(27)
led_3 = LED(17)

btn_1 = Button(26, pull_up=True, bounce_time=0.05)  # LED 1에 해당하는 버튼
btn_2 = Button(23, pull_up=True, bounce_time=0.05)  # LED 2에 해당하는 버튼
btn_3 = Button(24, pull_up=True, bounce_time=0.05)  # LED 3에 해당하는 버튼

# 점수를 출력하는 함수
def update_score():
    global score
    score += 1
    print(f"점수: {score}")
    bz.play(Tone(440.0))
    time.sleep(0.2)
    bz.stop()

# LED 깜빡임 함수 (각 LED는 랜덤 주기로 깜빡임)
def blink_led(led):
    global led_on_count  # 불이 켜진 횟수를 세기 위해 전역 변수 사용
    while True:
        # 주기를 매번 랜덤하게 설정 (0초 ~ 3초 사이)
        interval = random.uniform(0, 3)
        
        # LED를 0.5초 동안 켰다 끄기
        led.on()  # LED 켜기
        led_on_count += 1  # LED가 켜졌을 때 카운트 증가
        time.sleep(0.5)  # 0.5초 대기
        led.off()  # LED 끄기
        time.sleep(0.5)  # 0.5초 대기
        
        # 랜덤 주기만큼 대기 (주기마다 주기 변경)
        time.sleep(interval)

# 버튼 눌렸을 때 점수를 올려주는 함수
def btn_1_pressed():
    if led_1.is_lit:  # LED 1이 켜져 있을 때
        update_score()

def btn_2_pressed():
    if led_2.is_lit:  # LED 2가 켜져 있을 때
        update_score()

def btn_3_pressed():
    if led_3.is_lit:  # LED 3이 켜져 있을 때
        update_score()

# 각 버튼에 눌림 이벤트 핸들러 연결
btn_1.when_pressed = btn_1_pressed
btn_2.when_pressed = btn_2_pressed
btn_3.when_pressed = btn_3_pressed

# 각 LED를 위한 스레드 생성
thread_1 = threading.Thread(target=blink_led, args=(led_1,))
thread_2 = threading.Thread(target=blink_led, args=(led_2,))
thread_3 = threading.Thread(target=blink_led, args=(led_3,))

# 각 스레드를 daemon 스레드로 설정
thread_1.daemon = True
thread_2.daemon = True
thread_3.daemon = True

# 각 스레드 시작
thread_1.start()
thread_2.start()
thread_3.start()

# 30초 동안 프로그램 실행 후 결과 출력
start_time = time.time()

while True:
    # 30초 동안 대기
    elapsed_time = time.time() - start_time
    if elapsed_time >= 10:
        # 30초가 경과하면 종료
        print(f"불이 켜진 총 횟수: {led_on_count}")
        # 불이 켜진 횟수의 50% 이상이면 win
        if led_on_count > 0 and (led_on_count // 2) < score:
            print("win")
            play_scale(bz, notes, 1)
        else:
            print("lose")
        break

    time.sleep(1)  # 메인 루프에서 대기
