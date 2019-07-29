#!/usr/bin/python

i = 100
while i != 0:
    print(str(i)+" bottles of beer on the wall, "+str(i)+" bottles of beer")
    print("Take one down, pass it around, {0} bottles of beer on the wall.".format(i-1))
    i -=1
if i == 0:
    for i in range(100):
        print("No bottles of beer on the wall, no bottles of beer")
        print("Go to the store, buy some more, {} bottles of beer on the wall.".format(i))
