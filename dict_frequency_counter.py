#!/usr/bin/python
from collections import defaultdict, Counter

def dictCounter(x):
    counts = {}
    for i in x.split():
        counts[i] = counts.get(i, 0)+1
    return counts
print(dictCounter("Hello World Hello World"))

def defaultDictCounter(x):
    counts = defaultdict(int)
    for i in x.split():
        counts[i] += 1
    return counts
print(defaultDictCounter("Hello World Hello World"))

def collectionsCounter(x):
    counts = Counter(x.split())
    return counts

print(collectionsCounter("Hello World Hello World"))
