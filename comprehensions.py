#!/usr/bin/python

#List comprehension:
a = [k*k for k in range(1,10+1)]

#Set comprehension:
b = {k*k for k in range(1,10+1)}

#Generator comprehension:
c = (k*k for k in range(1,10+1))

#Dictionary comprehension:
d = {k:k*k for k in range(1,10+1)}

print("%s\n%s\n%s\n%s\n" %(a,b,next(c),d))
