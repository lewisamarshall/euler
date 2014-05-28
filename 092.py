#!/usr/bin/pypy

one_set = set([1])
en_set = set([89])


def square_sum(i):
    return sum([int(j)**2 for j in str(i)])

print square_sum(10)

for i in range(1, 10000000):
    temp_i = i
    temp_set = set()
    while temp_i not in one_set and temp_i not in en_set:
        temp_set.add(temp_i)
        temp_i = square_sum(temp_i)
    if temp_i in one_set:
        one_set |= temp_set
    elif temp_i in en_set:
        en_set |= temp_set

print len(en_set & set(range(1, 10000000)))
