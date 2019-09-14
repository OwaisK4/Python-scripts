#!/usr/bin/python
import random

#A = [1,5,3,8,6,2,6,5]
A = [random.randint(1,10) for i in range(20)]
for j in range(1,len(A)):
    key = A[j]
    i = j# - 1
    while (i > 0) and (A[i] < key):
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)
