#!/usr/bin/python

lis = []
i = 100
while i < 1000:
    i += 1
    if i % 3 == 0:
        lis.append(i)

print(lis)
print(sum(lis))
