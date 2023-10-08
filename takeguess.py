#!/usr/bin/python
import random

print("I am thinking of a number")
for guessesTaken in range(1,10):
    secretNumber = random.randint(1,10)
    guess = int(input())
    if guess < secretNumber:
        print("Too low")
    elif guess > secretNumber:
        print("Too high")
    else:
        break
if guess == secretNumber:
    print("Correct")
else:
    print("Nope")
