#!/usr/bin/env python
__author__ = "Alex Comiskey"

print(sum({i for i in [i*3 for i in range(1000)] if i < 1000}.union({i for i in [i*5 for i in range(1000)] if i < 1000})))
