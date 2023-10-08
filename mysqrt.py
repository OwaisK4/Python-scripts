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
    #print("a:\t\nmysqrt():\t\nsqrt():\t\ndiff():\t\n")
    for a in range(2,10):
        diff = sqrt(a)-mysqrt(a,a-1)
        print(" a:\t\t%s\n"%a, "mysqrt():\t%s\n"%mysqrt(a,a-1), "sqrt():\t%s\n"%sqrt(a), "diff():\t%s\n"%diff)

#print(a, mysqrt(a,a-1), sqrt(a), diff)
