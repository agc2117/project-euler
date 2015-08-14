#!/usr/bin/env python
"""
Enumerate the points on the grid, beginning at (0,0) and ending at (19,19).
Let 0 be a right, and 1 be a down. Randomly choose x in [0,1], and then round
to the nearest int to decide the step. Run until you reach (19,19), then repeat.
Repeat this ~1000000 times, then find the unique paths.

There's a relationship with the # of rational numbers here, if we conceive of this
problem in a similar way to Cantor's Proof that the cardinality of the rationals
is aleph0. 
"""
__author__ = "Alex Comiskey"

import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
final_point = Point(19,19)

def next_point(point):
    rndm = random.choice(range(0,1000))
    x = point.x
    y = point.y
    if point == final_point:
        return point
    elif x == 19:
        y = point.y + 1
    elif y == 19:
        x = point.x + 1
    elif rndm > 499:
        x = point.x + 1
    else:
        y = point.y + 1
    new_point = Point(x,y)
    return new_point

def path_walker(pt):
    path = []
    path.append(pt)
    new_pt = Point(pt.x, pt.y)
    while new_pt != final_point:
        new_pt = next_point(new_pt)
        path.append(new_pt)
    return path

def main():
    paths = []
    for i in range(1000000):
        initial_point = Point(0,0)
        path = path_walker(initial_point)
        if path not in paths:
            paths.append(path)
        print(len(paths))
    return paths
if __name__ == "__main__":
    main()
