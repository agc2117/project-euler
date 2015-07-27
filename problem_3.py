#!/usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
__author__ = "Dan Wagner"

from math import sqrt

def is_prime(num):
    # Guard clauses
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    # The actual prime test
    for idx in range(3, int(sqrt(num)) + 1, 2):
        if num % idx == 0:
            return False

    return True

# It's business time
start = 600851475143
sq = int(sqrt(600851475143))
for idx in range(sq, 0, -1):
    if start % idx == 0 and is_prime(idx):
        print(idx)
        break

