#!/usr/bin/python

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
for i in range(100):
    print(fibonacci(i),end=", ")
