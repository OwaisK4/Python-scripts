#!/usr/bin/python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
if __name__=="__main__":
    for i in range(100):
        print(fib(i),end=",")
