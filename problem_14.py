#!/usr/bin/env python
"""
Which starting number, under one million, produces the longest Collatz chain?
"""
__author__ = "Alex Comiskey"

def next_collatz(num):
    if num % 2:
        next_one = 3*num + 1
    else:
        next_one = num // 2
    return next_one

def collatz_chain(start):
    chain = []
    while start != 1:
        chain.append(start)
        start = next_collatz(start)
    return chain

chains = []
for i in range(1,1000000):
    chains.append(len(collatz_chain(i)))
    print(len(chains))

print("Longest chain is {0} and occurs at {1}".format(max(chains), chains.index(max(chains))+1))
    
