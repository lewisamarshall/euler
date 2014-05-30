#!/usr/bin/pypy
from math import sqrt
import decimal
import time
decimal.getcontext().prec = 14

n = int(10**9)
divisor = sqrt(decimal.Decimal(2))
print divisor

start = time.time()
while True:
    n += 1
    b = int(n//divisor+1)
    if 2*b*(b-1) == n*(n-1):
        break
print n, int(b)
print time.time()-start
