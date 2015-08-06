#!/usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
__author__ = "Alex Comiskey"

"""I'd like to solve this problem while avoiding importing packages,
    so we need to define a sqrt, to test whether an integer is prime.
    Additionally, in order to find an upper bound on the n-th prime,
    we can use the approximation that the n-th prime ~ n*ln(n), which
    means we will need to define a logarithm knowing that the logarithm
    is defined as the lim as n -> infinity of n*((x**(1/n) - 1), and
    using large n    
"""

def sqrt(num):
    if num == 0:
        return 0
    if num < 1:
        return None
    x = (num + 1) // 2
    for i in range(5):
        x = (x + num//x) // 2
    return x

def ln(num):
    n = 10000
    return n * ((num ** (1/n)) -1)

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for i in range(3, sqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True

prime_count = 10001
max_num = 2**(int(10001*ln(10001)).bit_length())

primes = [i for i in range(max_num) if is_prime(i)]

print(primes[10000])
