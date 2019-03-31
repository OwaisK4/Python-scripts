#!/usr/bin/python
import sys

total = 0
try:
    x = int(sys.argv[1])
except:
    x = 100
for i in range(x):
    total += i
print(total)

