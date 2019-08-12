#!/usr/bin/python
import argparse

def roots(a,b,c):
    D = (b**2 - 4*a*c)**0.5
    x1 = (-b + D)/2*a
    x2 = (-b - D)/2*a
    return(x1,x2)
parser = argparse.ArgumentParser()
parser.add_argument("a", action="store",type=int)
parser.add_argument("b",action="store",type=int)
parser.add_argument("c",action="store",type=int)
args = parser.parse_args()
if __name__ == "__main__":
    a = args.a
    b = args.b
    c = args.c
    x_1, x_2 = roots(a,b,c)
    print("x_1 root: %s\nx_2 root: %s" % (x_1,x_2))
