#!/usr/bin python
import math

total = 0

with open('input', 'r') as f:
    for line in f:
        val = int(line)
        val = math.floor(val/3)-2
        total += val

print(total)


