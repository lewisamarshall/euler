import itertools

computed = []

def pentagonal(n):
    p = int(n*(3*n-1)/2)
    if p not in computed:
        computed.append(p)
    return p

def is_pentagonal(p):
    if p in computed:
        return True

    # n = something
    if p>1000:
        return True

    n = 0.1

    return n==int(n)

for j in itertools.count(start=1, step=1):
    pj = pentagonal(j)
    for k in range(1, j):
        pk = pentagonal(k)

        if is_pentagonal(abs(pj-pk)):
            if is_pentagonal(pj+pk):
                raise StopIteration

print('j: {}\nk: {}\nD: {}'.format(j, k, pj-pk))
