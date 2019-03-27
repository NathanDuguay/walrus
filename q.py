from gpiozero import LED
from time import sleep

q = LED(17)

q.on()
sleep(1.5)
q.off()
sleep(0.5)
q.on()
sleep(1.5)
q.off()
sleep(0.5)
q.on()
sleep(0.5)
q.off()
sleep(0.5)
q.on()
sleep(1.5)
q.off()
sleep(1.5)
