#!/usr/bin/python
def fibonacci(n):
    #if n == 0:
    #    return 0
    #elif n == 1:
    #    return 1
    if n < 2:
        return n
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        return res
for i in range(100):
    print(fibonacci(i))

