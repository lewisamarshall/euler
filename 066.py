from math import sqrt


def is_square(n):
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


print is_square(9), is_square(12)


def diphantine(d):
    if sqrt(d) == int(sqrt(d)):
        return False
    y = 0
    while 1:
        y += 1
        x = sqrt(1 + d*y**2)
        if int(x) == x:
            return (int(x))
    # if is_square(d) or d == 0:
    #     return False
    # y = 0
    # while 1:
    #     y += 1
    #     x2 = 1 + d*y**2
    #     if is_square(x2):
    #         return (sqrt(x2))


minx = [diphantine(d) for d in range(2, 100)]
print(minx.index(max(minx)), max(minx))
