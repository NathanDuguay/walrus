from gpiozero import LED
from time import sleep

led = LED(17)

while True:
	led.on()
	sleep(1.5)
	led.off()
