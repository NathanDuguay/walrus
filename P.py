from gpiozero import LED
from time import sleep

p = LED(17)

p.on()
sleep(0.5)
p.off()
sleep(0.5)
p.on()
sleep(1.5)
p.off()
sleep(0.5)
p.on()
sleep(1.5)
p.off()
sleep(0.5)
p.on()
sleep(0.5)
p.off()
sleep(1.5)
