#!/usr/bin/python

def isAnagram(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False
    s1 = sorted(str1)
    s2 = sorted(str2)
    if s1 != s2:
        return False
    return True
if __name__ == '__main__':
    x = str(input('Enter first word:'))
    y = str(input('Enter second word:'))
    if isAnagram(x,y):
        print(x, 'and', y, 'are anagrams')
    else:
        print(x, 'and', y, 'are not anagrams')

