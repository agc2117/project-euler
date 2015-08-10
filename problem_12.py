#!/usr/bin/env python
"""First triangular number with 500 divisors"""
__author__ = "Alex Comiskey"

import math

def triangular_num(n):
    return int((n/2)*(n+1))

def num_divisors(num):
    divs = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            divs.append(i)
            divs.append(num//i)
    return len(divs)

def main():
    triangular_nums = [triangular_num(i) for i in range(1, 100001)]
    divs = []
    for i in triangular_nums:
        divs.append(num_divisors(i))
        print("{0} is max, currently at element number {1}".format(max(divs), len(divs)))
        if num_divisors(i) >= 500:
            print("{0} is the first triangular number with gt 500 divisors".format(i))
            break
    print(max(divs))
    return divs

main()

"""
Refactor with a Sieve of Atkin? Very, very slow performance?
"""
