from isprime import isprime
from itertools import permutations

digits=''.join(map(str, range(1,10)))
primes=[]
for i in reversed(range(1,10)):
    for nums in permutations(digits[:i], i):
        nums=''.join(nums)
        if isprime(int(nums)):
            primes.append(int(nums))
    if primes:
        break
print max(primes)
