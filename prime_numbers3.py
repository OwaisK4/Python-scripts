#!/usr/bin/python

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print("%s equals %s * %s" %(n,x,n//x))
            break
    else:
            print("%s is a prime number" % n)

