#!/usr/bin/python
# still needs debugging, even though I copied it from Programiz or something.
from argparse import ArgumentParser

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
            #continue
        #else:
            #print(num)
parser = ArgumentParser()
parser.add_argument("range",help="Upper bound of prime numbers",type=int)
args = parser.parse_args()
a = []
#if isinstance(args.range,int):
#   s = args.range
for i in range(args.range):
    if prime(i):
        a.append(i)
        print(i,end=",")
print(len(a))
