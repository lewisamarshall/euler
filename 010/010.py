from isprime import isprime
total=0
for i in range(2, 2*10**6):
    if isprime(i):
        total += i

print(total)
