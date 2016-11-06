def collatz(n, cd):
    i = 0
    n_orig = n
    n = int(n)

    while n not in cd:
        i += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1

    return cd.update({n_orig: cd[n] + i})

collatzdict = {1: 0}
max_route = 0
furthest = 1
for j in range(1, 10**6):
    collatz(j, collatzdict)
    if collatzdict[j] > max_route:
        max_route = collatzdict[j]
        furthest = j

print(furthest)
