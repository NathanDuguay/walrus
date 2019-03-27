from gpiozero import LED
from time import sleep

while True:
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)

	led.on()
	sleep(0.5)
	led.off()
