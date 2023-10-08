#!/usr/bin/python
from argparse import ArgumentParser
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if not isinstance(n,int):
        print("Factorial is only defined for integers")
    elif n < 0:
        print("Factorial is not  defined for negative integers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
parser = ArgumentParser()
parser.add_argument("range",help="Number to compute factorial of",type=int)
args = parser.parse_args()
for i in range(args.range+1):
    print(factorial(i))
