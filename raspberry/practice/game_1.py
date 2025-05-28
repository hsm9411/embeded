from gpiozero import LED, Button, Buzzer
from signal import pause

def is_R_match():
    if( led_R.is_lit() == True )
        score = score + 1
        bz.beep(on_time=0.2, off_time=0)


score = 0

bz = Buzzer(6)

led_R = LED(5)

btn_R = Button(26, pull_up=True, bounce_time=0.05)

btn_R.when_pressed = is_R_match()

while True:
    led_R.blink(on_time=0.5, off_time=0)
    on_time = random.uniform(0.5, 5.0)
    time.sleep(on_time) 
