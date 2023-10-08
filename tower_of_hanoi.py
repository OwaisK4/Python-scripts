#!/usr/bin/python
from argparse import ArgumentParser

def hanoi(x):
    res = (2**x) - 1
    return res
parser = ArgumentParser()
parser.add_argument("discs",help="Number of Tower discs",type=int)
args = parser.parse_args()
for i in range(args.discs+1):
    print("%s discs:\t%s" % (i,hanoi(i)))
