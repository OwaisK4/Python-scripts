#!/usr/bin/python
from time import sleep

def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n -= 1
    print("Blastoff!")
countdown(5)
