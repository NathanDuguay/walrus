from gpiozero import LED
from time import sleep

o = LED(17)

o.on()
sleep(1.5)
o.off()
sleep(0.5)
o.on()
sleep(1.5)
o.off()
sleep(0.5)
o.on()
sleep(1.5)
o.off()
sleep(1.5)
