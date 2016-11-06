digits = set(''.join(map(str, range(10))))

for i in permutations(digits, 3):
    if str(int(i)) == i:
        for j in permutations(digits-set(i), 2)
