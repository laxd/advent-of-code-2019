#!/usr/bin python
import math

total = 0

def calculate_fuel(mass):
    val = math.floor(mass/3)-2
    if(val <= 0):
        return 0
    return val + calculate_fuel(val)

with open('input', 'r') as f:
    for line in f:
        val = int(line)
        total += calculate_fuel(val)

print(total)


