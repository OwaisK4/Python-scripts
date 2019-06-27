#!/usr/bin/python
# still needs debugging, even though I copied it from Programiz or something.

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            continue
        else:
            print(num)
for i in range(100):
    print(prime(i))
