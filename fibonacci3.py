#!/usr/bin/python
import sys
#try:
    #i = int(sys.argv[1])
#except:
i = 1000
a,b = 0,1
#while a < i:
for x in range(i):
    print(a, end=',')
    a,b = b,a+b
