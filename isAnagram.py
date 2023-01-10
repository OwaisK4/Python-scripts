#!/usr/bin/python

def isAnagram(x,y):
    if sorted(x) == sorted(y):
        return True
f = open("file","w")
freq = {}
for i in f.read().split():
    freq[i] = freq.get(i,0) + 1
print(freq)


