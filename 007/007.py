from isprime import *

k = 0
i = 1
while k < 10001:
    i += 1
    if isprime(i):
        k += 1

print(i)
