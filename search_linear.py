#!/usr/bin/python
import argparse, random

def linear_search(array,x):
    for i in range(len(array)):
        if array[i] == x:
            return array,i
    print("x not found")

parser = argparse.ArgumentParser()
parser.add_argument("val",help="value to search for",type=int)
args = parser.parse_args()
print(linear_search([1,2,3,4,5,6,7,8,9,10],args.val))
