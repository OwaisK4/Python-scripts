#!/usr/bin/python
from sys import argv

total = 0
try:
    x = int(argv[1])
except:
    x = 101
for i in range(x):
    total += i
print(total)

