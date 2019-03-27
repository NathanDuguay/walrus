from gpiozero import LED
from time import sleep

l = LED(17)

l.on()
sleep(0.5)
l.off()
sleep(0.5)
l.on()
sleep(1.5)
l.off()
sleep(0.5)
l.on()
sleep(0.5)
l.off()
sleep(0.5)
l.on()
sleep(0.5)
l.off()
sleep(1.5)

