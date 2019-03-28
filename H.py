from gpiozero import LED
from time import sleep

led = LED(17)

While True:
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)
	led.on()
	sleep(0.5)
	led.off
