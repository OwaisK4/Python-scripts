#!/usr/bin/python
import sys
try:
    i = int(sys.argv[1])
except:
    i = 10
a,b = 0,1
while a < i:
    print(a)
    a,b = b,a+b
