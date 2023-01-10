#!/usr/bin/python
from math import sqrt

Phi = (1+sqrt(5))/2
phi = (1-sqrt(5))/2
for i in range(100):
    f = (Phi**i - phi**i)/sqrt(5)
    print("%sth fibonacci: " % i,round(f))
