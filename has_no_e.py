#!/usr/bin/python
from sys import argv
def has_no_e(x,avoid):
    for i in x:
        if i in avoid:
            return False
    return True
print(has_no_e(argv[1],argv[2]))

