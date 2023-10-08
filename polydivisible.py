#!/usr/bin/python
import argparse

def polydivisible(n):
    number = n
    digits = [x for x in str(n)]
    for i in range(1,len(digits) + 1):
        #a = "".join(digits[:i])
        a = int("".join(digits[:i]))
        if not a % i == 0:
            print("Number is not polydivisible")
            #break
            return digits
        print(a)
    print("Number is polydivisible")
    return digits
parser = argparse.ArgumentParser()
parser.add_argument("number", help="Number to check")
args = parser.parse_args()
print(polydivisible(args.number))
