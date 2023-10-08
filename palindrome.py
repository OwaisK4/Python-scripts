#!/usr/bin/python
import sys

x = str(sys.argv[1])
a = x[::-1]
if x == a:
    print(x, " is a palinrome")
else:
    print(x, " is not a palindrome")

