from gpiozero import PWMOutputDevice, Button
from time import sleep
import threading

# 부저
buzzer = PWMOutputDevice(12)

# 버튼 (풀업)
button = Button(26, pull_up=True)

# 마리오 멜로디
melody = [
    # Intro
    (659, 0.125), (659, 0.125), (0, 0.125), (659, 0.125), (0, 0.125),
    (523, 0.125), (659, 0.125), (0, 0.125), (784, 0.125), (0, 0.375),
    (392, 0.125), (0, 0.375),

    # Verse 1
    (523, 0.125), (0, 0.25), (392, 0.125), (0, 0.25), (330, 0.125),
    (0, 0.25), (440, 0.125), (0, 0.125), (494, 0.125), (0, 0.125),
    (466, 0.125), (0, 0.125), (440, 0.125), (0, 0.125), (392, 0.125),
    (659, 0.125), (784, 0.125), (880, 0.125), (698, 0.125),
    (784, 0.125), (659, 0.125), (523, 0.125), (587, 0.125),
    (494, 0.125),

    # Verse 2 (계속)
    (523, 0.125), (0, 0.25), (392, 0.125), (0, 0.25), (330, 0.125),
    (0, 0.25), (440, 0.125), (0, 0.125), (494, 0.125), (0, 0.125),
    (466, 0.125), (0, 0.125), (440, 0.125), (0, 0.125), (392, 0.125),
    (659, 0.125), (784, 0.125), (880, 0.125), (698, 0.125),
    (784, 0.125), (659, 0.125), (523, 0.125), (587, 0.125),
    (494, 0.125),

    # 엔딩 느낌
    (784, 0.125), (740, 0.125), (698, 0.125), (622, 0.125),
    (659, 0.375), (0, 0.125), (659, 0.25),
    (523, 0.125), (587, 0.125), (494, 0.25),
    (523, 0.125), (392, 0.125), (330, 0.25),
    (440, 0.125), (494, 0.125), (466, 0.125),
    (440, 0.125), (392, 0.125), (659, 0.125), (784, 0.125)
]


# 배속 리스트
speeds = [1.0, 1.5, 0.5]
speed_index = 0
speed_multiplier = speeds[speed_index]

# 멜로디 실행 제어
running = True

# 멜로디 재생 스레드
def play_melody():
    global speed_multiplier
    while running:
        for freq, duration in melody:
            if freq == 0:
                buzzer.value = 0
            else:
                buzzer.frequency = freq
                buzzer.value = 0.8
            sleep(duration * speed_multiplier)
        sleep(1.0)

# 버튼 누르면 배속 변경
def change_speed():
    global speed_index, speed_multiplier
    speed_index = (speed_index + 1) % len(speeds)
    speed_multiplier = speeds[speed_index]
    print(f"배속 변경: {speed_multiplier}배속")

try:
    # 스레드 실행
    threading.Thread(target=play_melody, daemon=True).start()
    button.when_pressed = change_speed

    while True:
        sleep(1)

except KeyboardInterrupt:
    running = False
    buzzer.value = 0
    print("\n프로그램 종료됨.")
