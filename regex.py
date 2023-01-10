#!/usr/bin/python
import sys, re

numberRegex = re.compile(r"\d{11}")
no = numberRegex.search(sys.argv[1])
try:
    print(no.group())
except:
    print("Wrong no.")


