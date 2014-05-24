from factors import *

n=1
triangle=0
divs = [1]
while len(divs) < 500:
    triangle += n
    n += 1
    factors = factorize(triangle)
    divs = divisors(factors)

print triangle
