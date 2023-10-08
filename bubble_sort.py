#!/usr/bin/python

#TODO: Fix this damn thing
def bubble_sort(array):
    x = array
    for i in range(len(x) - 1):
        if x[i] > x[i+1]:
            x[i],x[i+1] = x[i+1],x[i]
    return x
list = [7,3,9,4,6,2,0,1]
print("Unsorted array: %s\nSorted array: %s" % (list,bubble_sort(list)))
