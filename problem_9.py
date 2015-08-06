#!/usr/bin/env python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
__author__ = "Alex Comiskey"

basic = (3,4,5)
secondary = (8,12,13)

def test_if_sums_to_thousand(triplet):
    try:
        triple_sum = triplet[0]+triplet[1]+triplet[2]
        if (1000//triple_sum)*(triple_sum) == 1000:
            return 1000//triple_sum
    except TypeError:
        return False

    return False

#Both the basic and secondary elementary triplets fail this test, so we need
#to look for a new one! We will take as input a single integer, and output the
#first triplet that works with it

def sqrt(num):
    if num == 0:
        return 0
    if num < 1:
        return None
    x = (num + 1) // 2
    for i in range(5):
        x = (x + num//x) // 2
    return int(x)

def is_perfect_square(n):
    root = sqrt(n)
    if root**2 == n:
        return True
    return False

def find_triplet(n):
    for i in range(n+1, 1000):
        c_squared = n**2 + i**2
        if is_perfect_square(c_squared):
            return (n, i, sqrt(c_squared))
    return None


for i in range(2,100):
    triplet = find_triplet(i)
    divisor = test_if_sums_to_thousand(triplet)
    if divisor:
        new_triplet = tuple([i*divisor for i in triplet])
        print(new_triplet[0]*new_triplet[1]*new_triplet[2])
        
