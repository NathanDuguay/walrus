from gpiozero import LED
from time import sleep
import re

led =  LED(17)

mot = input("Que voulez-vous dire?")

for letter in mot:

    if letter == " ":

        exec(open("space.py").read())

    else:

        pyFile = letter.upper() + ".py"

        exec(open(pyFile).read())

print("Do me again")

sleep(30)
