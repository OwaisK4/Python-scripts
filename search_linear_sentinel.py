#!/usr/bin/python
import argparse

def sentinel_search(A,x):
    n = len(A)-1
    last,A[n] = A[n],x
    i = 0
    while A[i] != x:
        i += 1
    A[n] = last
    if (i < n) or (A[n] == x):
        return i
    else:
        return "Not Found"
parser = argparse.ArgumentParser()
parser.add_argument("val",type=int,help="Value to search for in list")
args = parser.parse_args()
a = [1,6,3,9,7,2,5,4,8,10]
print(sentinel_search(a,args.val),a)
