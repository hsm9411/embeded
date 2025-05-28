from gpiozero import Buzzer
from time import sleep

bz = Buzzer(12)
bz.on()

for b in range(101):
    bz.value = b*100
    sleep(1)

bz.off()
