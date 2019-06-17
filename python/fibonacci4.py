#!/usr/bin/python
import sys
try:
    i = int(sys.argv[1])
except:
    i = 50
def fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b = b,a+b
print(fibonacci(i))
