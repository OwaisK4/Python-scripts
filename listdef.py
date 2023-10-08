#!/usr/bin/python

def f(a,l=[]):
    l.append(a)
    return l
for i in range(10):
    print(f(i))
