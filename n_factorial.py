#!/usr/bin/python
import math

for i in range(200):
    n = str(math.factorial(i))
    if n.count("0") > 24:
        print(n, i)
        break
