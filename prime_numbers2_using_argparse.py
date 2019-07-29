#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:27:25 2019

@author: Owais Ali Khan
"""
import argparse
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def printPrime(n):
    for i in range(2, n+1):
        if isPrime(i):
            print(i, end=',')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("range",help="The number of prime numbers between 2 and range",type=int)
    args = parser.parse_args()
    print(printPrime(args.range))
