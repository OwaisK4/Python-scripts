#!/usr/bin/python
import argparse
def pi(n_terms):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for i in range(n_terms):
        pi += operation * (numerator/denominator)
        operation *= -1.0
        denominator += 2.0
    return pi
if __name__=="__main__":
    parser = argparse.ArgumentParser()

    print(pi())
