#!/usr/bin/env python
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
__author__ = "Dan Wagner"

def is_palindrome(num):
    forward = str(num)
    backward = str(num)[::-1]
    return forward == backward and str(num) != "0"

rng = range(999, -1, -1)
max_palindrome = 1
for x in rng:
    for y in rng:
        if is_palindrome(x * y) and (x * y > max_palindrome):
            max_palindrome = x * y

print(max_palindrome)

