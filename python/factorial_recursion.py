#!/usr/bin/python

def factorial(n):
    if not isinstance(n,int):
        print("Factorial is only defined for integers")
    elif n < 0:
        print("Factorial is not  defined for negative integers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
for i in range(10+1):
    print(factorial(i))
