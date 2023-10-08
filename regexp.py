#!/usr/bin/python
import os

a = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
#b = a.strip("")
#os.system("sed -i 's///g' regexp.py")
print(a)
print(a.count("$"))
count = 0
for i in a:
    if i == "$":
        count += 1
print(count)
print(a.find("$"))
def in_both(word1, word2):
    for i in word1:
        if i in word2:
            print(i)
in_both("apples","oranges")

d = dict()
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


