from gpiozero import LED
from time import sleep

ledR = LED(17)
ledG = LED(27)
ledB = LED(22)

while True:
    ledR.on()
    sleep(0.5)
    ledG.on()
    sleep(0.5)
    ledB.on()
    sleep(0.5)
    ledR.off()
    sleep(0.5)
    ledG.off()
    sleep(0.5)
    ledB.off()
    sleep(0.5)