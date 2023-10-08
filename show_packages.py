#!/usr/bin/python
import os

f = open("pip_packages")
for i in f.readlines():
    print(os.system("pip show %s" % i))
