#!/usr/bin/python
from math import sqrt

def mysqrt(a,x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
            break
        x = y
if __name__=='__main__':
    print("a"," "*len("a"), "mysqrt()"," "*len("mysqrt()"), "sqrt()"," "*len("sqrt()"), "diff()")
    for a in range(2,10):
        diff = sqrt(a)-mysqrt(a,a-1)
        print(a, mysqrt(a,a-1), sqrt(a), diff)



