pfactors = [2, 3, 5, 7, 11, 13, 17, 19]
factor_number = [0]*8
for n in range(1, 20):
    for idx, val in enumerate(pfactors):
        j = 0
        m = n
        while m % val == 0:
            j += 1
            m = m/val
        if j > factor_number[idx]:
            factor_number[idx] = j

product = 1
for idx, val in enumerate(pfactors):
    product = product*val**factor_number[idx]
print product
