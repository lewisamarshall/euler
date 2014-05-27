from fractions import Fraction
import time
start_time = time.time()

rationals = []
for i in range(1, 12001):
    rationals += [Fraction(j, i) for j in range(i//3+1, i//2+1)]
rationals = set(rationals)
print len(rationals)-1
print time.time() - start_time, "seconds"
