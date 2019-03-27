from gpiozero import LED
from time import sleep

m = LED(17)

m.on()
sleep(1.5)
m.off()
sleep(0.5)
m.on()
sleep(1.5)
m.off()
sleep(1.5)
