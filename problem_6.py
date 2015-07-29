#!/usr/bin/env python
"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
__author__ = "Alex Comiskey"

import sys

def sum_squares(n):
    return sum([s**2 for s in range(1,n+1)])

def square_sums(n):
    return sum(range(1,n+1))**2

f = sys.stdin
n = int(sys.argv[1])
print(square_sums(n) - sum_squares(n))
