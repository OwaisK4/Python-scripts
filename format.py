#!/usr/bin/python
import sys

quality = ' '.join(sys.argv[1:])
string = "Ahmer is a very %s boy" % quality
print(string)
