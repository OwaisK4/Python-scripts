#!/usr/bin/python
import os

for i in os.listdir("/data/data/com.termux/files/home/code/python"):
    print(os.path.getsize(os.path.join("/data/data/com.termux/files/home/code/python",i)))
