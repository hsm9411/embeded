from gpiozero import Button
from gpiozero import LED

btn = Button(17, pull_up=True)
led = LED(25)
# 상태 변수 선언
led_state = False  # 초기 상태 (False: 꺼짐, True: 켜짐)

# 현재 상태에 따라 반대 동작 실행
def toggle_led():
    global led_state  # 글로벌 변수로 상태를 추적
    if led_state:
        led.off()  # LED 끄기
    else:
        led.on()   # LED 켜기
    led_state = not led_state  # 상태 반전



while True:
    btn.wait_for_press()
    toggle_led()
    btn.wait_for_release()
