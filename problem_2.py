#!/usr/bin/env python
__author__ = "Alex Comiskey"

def fib(n):
    x = [1,2]
    while len(x) < n:
        x.append(x[-1] + x[-2])
    return x

for i in range(100):
    if max(fib(i)) < 4000000:
        fibs = fib(i)

print(sum([i for i in fibs if i % 2 == 0]))
