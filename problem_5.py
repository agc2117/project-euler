#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
__author__ = "Alex Comiskey"


#Check whether number is divisible by all number is a range
def is_divisible(num, divisor_range):
    max_divisor = 1
    for x in divisor_range:
        if num % x == 0:
            max_divisor = x
        else:
            break
    if max_divisor == max(divisor_range):
        return num
    else:
        return False

rng = range(1,1000000000)
for x in rng:
    if is_divisible(x, range(1,21)):
        break
print(x)
    
