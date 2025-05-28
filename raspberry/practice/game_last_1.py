from gpiozero import LED, Button, PWMOutputDevice
import random
import time
import threading

# 전역 변수로 score 선언
score = 0
led_on_count = 0  # 불이 켜진 횟수를 세는 변수




# 음계 주파수 (도레미파솔)
notes = {
    "C": 261.63,  # 도
    "D": 293.66,  # 레
    "E": 329.63,  # 미
    "F": 349.23,  # 파
    "G": 392.00   # 솔
}

# 음을 부저로 출력하는 함수
def play_note(buzzer, frequency, duration):
    buzzer.frequency = frequency  # 부저의 주파수 설정
    buzzer.value = 0.5  # 소리 크기 설정 (0.5는 중간 크기)
    time.sleep(duration)  # 주어진 시간 동안 소리 재생
    buzzer.value = 0  # 소리 끄기

# 도레미파솔 음계를 차례대로 출력하는 함수
def play_scale(buzzer):
    # 도레미파솔 순서대로 출력
    for note, freq in notes.items():
        play_note(buzzer, freq, 0.5)  # 각 음을 0.5초 동안 재생

# 점수를 출력하는 함수
def update_score():
    global score
    score += 1
    print(f"점수: {score}")
    play_note(bz, 329.63, 0.2)  # 'E' 음을 출력

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


# 부저, LED, 버튼 초기화
bz = PWMOutputDevice(12)  # 부저 초기화

led_1 = LED(5)
led_2 = LED(27)
led_3 = LED(17)

btn_1 = Button(26, pull_up=True, bounce_time=0.05)  # LED 1에 해당하는 버튼
btn_2 = Button(23, pull_up=True, bounce_time=0.05)  # LED 2에 해당하는 버튼
btn_3 = Button(24, pull_up=True, bounce_time=0.05)  # LED 3에 해당하는 버튼

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
            play_scale(bz)  # 게임 승리시 도레미파솔 음계 출력
        else:
            print("lose")
            play_scale(bz)
        break

    time.sleep(1)  # 메인 루프에서 대기
