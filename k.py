from gpiozero import LED
from time import sleep

k = LED(17)

k.on()
sleep(1.5)
k.off()
sleep(0.5)
k.on()
sleep(0.5)
k.off()
sleep(0.5)
k.on()
sleep(1.5)
k.off()
sleep(1.5)
