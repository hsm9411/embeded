from gpiozero import LED
import random
import time
import threading

# 3개의 LED 초기화
led_1 = LED(5)
led_2 = LED(27)
led_3 = LED(17)

# LED 깜빡임 함수 (각 LED는 랜덤 주기로 깜빡임)
def blink_led(led):
    while True:
        # 주기를 매번 랜덤하게 설정 (0초 ~ 3초 사이)
        interval = random.uniform(0, 3)
        
        # LED를 0.5초 동안 켰다 끄기
        led.on()  # LED 켜기
        time.sleep(0.5)  # 0.5초 대기
        led.off()  # LED 끄기
        time.sleep(0.5)  # 0.5초 대기
        
        # 랜덤 주기만큼 대기 (주기마다 주기 변경)
        time.sleep(interval)

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

# 메인 스레드는 기다리기만 함
while True:
    time.sleep(1)
