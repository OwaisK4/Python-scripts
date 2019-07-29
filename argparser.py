# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:00:40 2019

@author: Owais Ali Khan
"""

import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo",help="echo the strings you supply here")
parser.add_argument("square",help="square of supplied numbers",type=int) 
args = parser.parse_args()
#print(args.echo)
print(args.square**2)
