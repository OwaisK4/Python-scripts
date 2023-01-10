#!/usr/bin/python
import sys
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    pascal = [[1]]
    for i in range(1, numRows):
        pascal.append([1])
        for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
            pascal[-1].append(num1 + num2)
        pascal[-1].append(1)
    return pascal
#print(generate(numRows=5))
a = generate(numRows=15)
for i in range(15):
    print(" "*(10-len(a[i])),a[i])
