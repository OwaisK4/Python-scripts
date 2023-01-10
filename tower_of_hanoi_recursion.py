#!/usr/bin/python
from argparse import ArgumentParser

discs = {0:0,1:1,2:3}
def hanoi(x):
    #if x < 2:
    #    return x
    if x in discs:
        return discs[x]
    discs[x] = (2 * discs[x-1]) + 1
    return discs[x]
parser = ArgumentParser()
parser.add_argument("range",help="Number of discs in tower",type=int)
args = parser.parse_args()
for i in range(args.range):
    print("%s discs:\t%s" % (i,hanoi(i)))
