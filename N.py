from gpiozero import LED
from time import sleep

n = LED(17)

n.on()
sleep(1.5)
n.off()
sleep(0.5)
n.on()
sleep(0.5)
n.off()
sleep(1.5)
