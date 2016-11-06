#!/usr/bin/pypy
from math import sqrt
import decimal
import time


def prob_check(b, n):
    if 2*(b**2-b) == (n**2-n):
        return True
    else:
        return False


def calc_blueprob():
    decimal.getcontext().prec = 14

    n = int(2*10**3)
    divisor = sqrt(2.0)
    print divisor

    start = time.time()
    for n in range(2*10**6, 10**7):
        # while True:
        # n += 1
        b = int(n//divisor+1)
        if prob_check(b, n):
            break
    print n, int(b)
    print time.time()-start

calc_blueprob()
