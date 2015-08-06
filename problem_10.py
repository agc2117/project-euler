#!/usr/bin/env python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
__author__ = "Alex Comiskey"

#Repurposing code from Problem 7

def sqrt(num):
    if num == 0:
        return 0
    if num < 1:
        return None
    x = (num + 1) // 2
    for i in range(5):
        x = (x + num//x) // 2
    return x

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for i in range(3, sqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True

print(sum([i for i in range(2000000) if is_prime(i)]))
