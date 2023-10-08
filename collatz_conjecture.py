#!/usr/bin/python
from sys import argv
def sequence(n):
    while n != 1:
        print(n,end=', ')
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
sequence(int(argv[1]))
