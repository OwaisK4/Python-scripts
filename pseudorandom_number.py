#!/usr/bin/python
from secrets import token_bytes

def random_key(length):
    tb = token_bytes(length)
    return tb, int.from_bytes(tb,"big")
for i in range(10):
    print(random_key(i))
