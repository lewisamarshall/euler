limit = 600851475143
i = 2
n = limit
while i*i < n:
    while n % i == 0:
        n = n/i
    i = i+1
print(n)
