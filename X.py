from gpiozero import LED
from time import sleep

led = LED(17)
led.on()
sleep(1.5)
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
sleep(1.5)
led.off()
