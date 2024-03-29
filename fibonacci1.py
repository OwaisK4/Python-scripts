#!/usr/bin/python
from typing import Dict

memo: Dict[int, int] = {0:0, 1:1}
def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
for i in range(100):
    print("%sth fibonacci:\t%s" % (i,fib(i)))

