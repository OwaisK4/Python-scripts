#!/usr/bin/python
from random import randint

di = dict(zip("abcd",range(4)))
biggest = 0
for val in di:
    if di[val] > biggest:
        biggest = di[val]
print(biggest)

li = [randint(0,10) for i in range(10)]
biggest_index = 0
for i in range(len(li)):
    if li[i] > li[biggest_index]:
        biggest_index = i
print(li)
print(biggest_index)
