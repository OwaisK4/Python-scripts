import math
import time
class animals():
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.legs = legs
class dog(animals):
    def bark(self):
        print("Woof")
class cat(animals):
    def purr(self):
        print("Meow")
Tommy = cat("Tommy", "Black", 4)
print(Tommy.purr())
time.sleep(1)
Husky = dog("Husky", "Brown", 4)
print(Husky.bark())
time.sleep(1)
print(math.pi)
def div(x):
    try:
        s = x / 0
        print(s)
    except ZeroDivisionError:
        print("Invalid function")
time.sleep(1)
print(div(5))
