#!/usr/bin/env python
__author__ = "Alex Comiskey"

import sys

def sum_squares(n):
    return sum([s**2 for s in range(1,n+1)])

def square_sums(n):
    return sum(range(1,n+1))**2

f = sys.stdin
n = int(sys.argv[1])
print(square_sums(n) - sum_squares(n))
