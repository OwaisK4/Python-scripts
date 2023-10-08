#!/usr/bin/python

def read_words(x):
    words = dict()
    for c in x:
        if c not in words:
            words[c] = 1
        else:
            words[c] += 1
    return words
def easy_dict(x):
    res = dict(zip(x, range(len(x))))
    return res
#a = "Hello World"
a = "Nothing at last is sacred but the integrity of one's own mind. –Ralph Waldo Emerson, Self-Reliance and Other Essays"

print(read_words(a.split()))
print(easy_dict(a.split()))
