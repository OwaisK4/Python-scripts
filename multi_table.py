#!/usr/bin/python
import argparse

def multi_table(x):
    for i in range(1,11):
        print("%s x %s = %s" % (x,i,x*i))
    return
parser = argparse.ArgumentParser()
parser.add_argument("number",help="Number to compute table of",type=float)
args = parser.parse_args()
print(multi_table(args.number))
