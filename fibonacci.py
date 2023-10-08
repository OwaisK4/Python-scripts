#!/usr/bin/python

fib = [1,1]
while  True:
    x = fib[-2] + fib[-1]
    #if  x%12  ==  0:
    if len(fib) > 40:
        break
    fib.append(x)
    #print(fib)
#print(fib)
for i in range(len(fib)-1):
    print(fib[i],end=", ")
