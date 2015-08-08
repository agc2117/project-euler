#!/usr/bin/env python
__author__ = "Alex Comiskey"

def prod(window):
    prod = int(window[0])
    for i in range(1,len(window)):
        prod = prod * int(window[i])
    return prod

def window_product(line):
    windows = [line[i:i+4] for i in range(len(line) - 3)]
    return max([prod(i) for i in windows])

def transpose(array):
    return [[x[i] for x in array] for i in range(len(array))]

def diagonal_right_window(flat):
    window = []
    for i, e in enumerate(flat):
        if (i % 17) + (i % 18) + (i % 19):
            continue
        elif i > 336:
            continue

        window.append([flat[i], flat[i+21], flat[i+42], flat[i+63]])
    return max([prod(i) for i in window])

def diagonal_left_window(flat):
    window = []
    for i, e in enumerate(flat):
        if i == 0 or i == 1 or i == 2:
            continue
        elif (i % 20 == 0) or ((i - 1) % 20 ==0) or ((i - 2) % 20 ==0):
            continue
        elif i > 336:
            continue
        
        window.append([flat[i], flat[i + 19], flat[i + 38], flat[i + 57]])
    return max([prod(i) for i in window])

def main():
    with open("num_11.txt", "r") as f:
        content = [x.strip('\n').split(' ') for x in f.readlines()]
        
    flatten = []
    for x in content:
        for i in x:
            flatten.append(i)

    horizontal = max(window_product(x) for x in content)
    vertical = max(window_product(x) for x in transpose(content))
    right_diagonal = diagonal_right_window(flatten)
    left_diagonal = diagonal_left_window(flatten)
    return max([horizontal, vertical, right_diagonal, left_diagonal])

four_max = main()
print(four_max)
