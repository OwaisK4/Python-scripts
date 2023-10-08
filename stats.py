#!/usr/bin/python
import math

def median(n):
    if n % 2 == 0:
        med = (n+1)/2
    else:
        med = (n+1)/2+(n-1)/2
    return med
print(median(7))
