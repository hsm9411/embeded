from gpiozero import LED, Button, PWMOutputDevice
import random
import time
import threading

# 전역 변수 선언
score = 0  # 플레이어의 점수
led_on_count = 0  # LED가 켜진 총 횟수

# 스레드 종료를 위한 이벤트 객체 생성
# 각 LED 스레드가 이 이벤트를 확인하여 종료 시점을 알 수 있도록 합니다.
stop_event = threading.Event()

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

# 점수를 올리고 소리를 내는 함수
def update_score():
    global score
    score += 1
    print(f"점수: {score}")
    play_note(bz, 329.63, 0.2)  # '미' 음을 짧게 출력

# LED 깜빡임 함수 (각 LED는 랜덤 주기로 깜빡임)
# 이제 stop_event를 확인하여 안전하게 종료됩니다.
def blink_led(led, event):
    global led_on_count
    while not event.is_set():  # 이벤트가 설정되지 않은 동안 (즉, 종료 신호가 없을 때까지) 반복
        # 주기를 매번 랜덤하게 설정 (0초 ~ 3초 사이)
        interval = random.uniform(0, 3)

        # LED를 0.5초 동안 켰다 끄기
        led.on()  # LED 켜기
        led_on_count += 1  # LED가 켜졌을 때 카운트 증가
        
        # event.wait()을 사용하여 sleep 중에도 종료 신호를 받을 수 있도록 함
        if event.wait(0.5): # 0.5초 대기, 만약 이 시간 내에 이벤트가 설정되면 즉시 반환
            break # 이벤트가 설정되면 루프 종료
        
        led.off()  # LED 끄기
        if event.wait(0.5): # 0.5초 대기
            break

        # 랜덤 주기만큼 대기 (주기마다 주기 변경)
        if event.wait(interval): # 랜덤 주기만큼 대기
            break
    
    # 스레드 종료 시 LED를 확실히 끄기
    led.off()
    print(f"DEBUG: LED {led.pin.number} 스레드 종료.")


# 버튼이 눌렸을 때 점수를 올려주는 함수들
def btn_1_pressed():
    if led_1.is_lit:
        update_score()

def btn_2_pressed():
    if led_2.is_lit:
        update_score()

def btn_3_pressed():
    if led_3.is_lit:
        update_score()

# --- GPIO 초기화 ---
bz = PWMOutputDevice(12)

led_1 = LED(5)
led_2 = LED(27)
led_3 = LED(17)

btn_1 = Button(26, pull_up=True, bounce_time=0.05)
btn_2 = Button(23, pull_up=True, bounce_time=0.05)
btn_3 = Button(24, pull_up=True, bounce_time=0.05)

# 각 버튼에 눌림 이벤트 핸들러 연결
btn_1.when_pressed = btn_1_pressed
btn_2.when_pressed = btn_2_pressed
btn_3.when_pressed = btn_3_pressed

# --- 스레드 생성 및 관리 ---
# 각 LED 깜빡임을 위한 별도의 스레드 생성
# 이제 stop_event를 인자로 전달합니다.
thread_1 = threading.Thread(target=blink_led, args=(led_1, stop_event))
thread_2 = threading.Thread(target=blink_led, args=(led_2, stop_event))
thread_3 = threading.Thread(target=blink_led, args=(led_3, stop_event))

# 데몬 스레드 설정을 제거합니다.
# thread_1.daemon = True
# thread_2.daemon = True
# thread_3.daemon = True

# 각 스레드 시작
thread_1.start()
thread_2.start()
thread_3.start()

# --- 게임 메인 루프 ---
start_time = time.time()

print("게임 시작! 10초 동안 불이 켜진 LED를 눌러 점수를 획득하세요!")

try:
    while True:
        elapsed_time = time.time() - start_time
        
        if elapsed_time >= 10:  # 10초가 경과하면 게임 종료
            print("\n--- 게임 종료 ---")
            break # 루프를 빠져나와 finally 블록으로 이동

        time.sleep(0.1)  # 메인 루프에서 대기
except KeyboardInterrupt:
    print("\nCtrl+C 감지됨, 게임 종료 중...")
finally:
    # 게임 종료 신호 보내기
    print("스레드 종료 신호 보냄...")
    stop_event.set() # stop_event를 설정하여 모든 blink_led 스레드에 종료 신호를 보냅니다.

    # 모든 스레드가 종료될 때까지 기다림 (join)
    # 이 부분이 중요합니다. 스레드들이 안전하게 I/O 작업을 마무리하고 종료될 시간을 줍니다.
    thread_1.join()
    thread_2.join()
    thread_3.join()
    print("모든 스레드 종료 완료.")

    # 최종 결과 출력
    print(f"불이 켜진 총 횟수: {led_on_count}")
    print(f"획득 점수: {score}")

    # 승리/패배 조건 판별
    if led_on_count > 0 and (led_on_count / 2) < score:
        print("축하합니다! WIN!")
        play_scale(bz)
    else:
        print("아쉽네요! LOSE!")
        play_scale(bz)
    
    # GPIO 자원 해제 (옵션이지만 명시적으로 해제하는 것이 좋습니다)
    bz.close()
    led_1.close()
    led_2.close()
    led_3.close()
    btn_1.close()
    btn_2.close()
    btn_3.close()
    print("GPIO 자원 해제 완료.")