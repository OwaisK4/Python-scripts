#!/usr/bin/python

fib = [1,1]
while  True:
    x = fib[-2] + fib[-1]
    if  x%12  ==  0:
        break
    fib.append(x)
    print(fib)
