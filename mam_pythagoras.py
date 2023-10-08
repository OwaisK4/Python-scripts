#!/usr/bin/python
from random import randint as rdint

nums = [(rdint(0,100),rdint(0,100)) for i in range(10)]
print(nums)
def pythagoras(lis):
    for i in range(len(lis)):
        m,n = lis[i]
        a = 2*m*n
        b = m**2 - n**2
        c = m**2 + n**2
        print("m = %s, n= %s" % (m,n))
        print("a = %s, b = %s, c = %s" % (a,b,c))
        print("c^2 = a^2 + b^2")
        print("%s  =  %s +  %s" % (c**2,a**2,b**2))
        print("%s  =  %s" % (c**2,a**2 + b**2))
        print("-"*10)
    return
print(pythagoras(nums))
