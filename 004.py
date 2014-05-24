from math import floor


def ispal(x):
    x = str(x)
    for i in range(0, int(floor(len(x)))):
        if not x[i-1] == x[-i]:
            return 0
    return 1

pal_list = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if ispal(i*j):
            pal_list.append(i*j)
print(max(pal_list))
