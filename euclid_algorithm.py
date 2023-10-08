#!/usr/bin/python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a < b:
    a,b = b,a
while b:
    a,b = b,a % b
    print(a)
