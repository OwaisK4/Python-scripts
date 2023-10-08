#!/usr/bin/python
import argparse

def even(i):
#   try:
#       i = int(i)
#   except:
#       print("Not a number.")
    return i % 2 == 0
def evenImproved(i):
    if len(str(i)) > 1:
        int x = str(i)[-1]
        return x % 2 == 0
    else:
        return i % 2 == 0
parser = argparse.ArgumentParser()
parser.add_argument("value",help="Number to check",type=int)
args = parser.parse_args()
print(even(args.value))
