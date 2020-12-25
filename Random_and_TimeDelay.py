#!/usr/bin/python3
import time
import random
x=0
print("Please enjoy your advertisement.")
advertisement = ["Purchase a Costco membership today!\n",
"Act Now and buy the PS5 today!","Use Mastercard and save more\n"]
randomad = random.choice(advertisement)
while x<20:
    print(randomad)
    time.sleep(5)
    x=x+1
    randomad = random.choice(advertisement)