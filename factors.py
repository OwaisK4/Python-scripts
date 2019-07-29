#!/usr/bin/python
import argparse

def factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number",help="number to get factors of",type=int)
    args = parser.parse_args()
    #try:
    #    b = int(args.number)
    #except ValueError:
    #    print("Not an integer")
    b = args.number
    if b > 0:
        factors(b)
    else:
        print("Enter a valid integer greater than zero")
