# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:09:04 2019

@author: Owais Ali Khan
"""

import os
os.chdir("E:")
path = os.getcwd()
for i in os.listdir(path):
    print(i,os.path.getsize(os.path.join(path,i)))
print(os.path.getsize.__doc__)
a = os.listdir(path)
for i in range(len(a)):
    print(a[i])
    s = a[i]
