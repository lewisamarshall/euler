#!/usr/bin/pypy
from math import sqrt


def isosceles_area(a, b):
    return a/2*sqrt(b**2-(a**2)/4)

print isosceles_area(6, 5)

total = 0
for a in range(1, 1000000000//3):
    for b in [a-1, a+1]:
        area = isosceles_area(a, b)
        if area == int(area):
            total += a+2*b

print total
