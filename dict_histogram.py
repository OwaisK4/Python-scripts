#!/usr/bin/python

def histogram(x):
    d = dict()
    for i in sorted(x):
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
def print_hist(x):
    for i in x:
        print(i,x[i])
h = histogram("brontosaurus")
print(h)
print(h.get("a",0))
print_hist(h)
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
print(reverse_lookup(h, 2))


