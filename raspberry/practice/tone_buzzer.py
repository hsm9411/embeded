from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

b = TonalBuzzer(12)
b.play(Tone("A4"))
sleep(2)
b.play(Tone(220.0)) # Hz
sleep(2)
b.play(Tone(60)) # middle C in MIDI notation
sleep(2)
b.play("A4")
sleep(2)
b.play(220.0)
sleep(2)
b.play(60)
