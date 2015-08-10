#!/usr/bin/env python
""""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
"""
__author__ = "Alex Comiskey"

with open("num_13.txt", "r") as f:
    nums = [int(x.strip('\n')) for x in f.readlines()]


num_sum = str(sum(nums))

print(num_sum[0:10])
