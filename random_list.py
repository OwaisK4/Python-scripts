#!/usr/bin/python
import random as rd
"""
data = []
for i in range(20):
    if not rd.randint(0,i) in data:
        data.append(rd.randint(0,20))
print(data, len(data))
"""
data = []
while len(data) < 20:
    if not rd.randint(0,50) in data:
        data.append(rd.randint(0,50))
    data = list(set(data))
print(data, len(data))
