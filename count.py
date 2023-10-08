#!/usr/bin/python
import sys

a = sys.argv[1]
if a.count(".") != 3:
    print("Not an IP address")
else:

    print(a," is a valid IP address")
