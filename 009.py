for a in range(1, 1000):
    for b in range(1, 1000):
        c = (a**2 + b**2)**.5
        if (a**2+b**2) == (1000-a-b)**2:
            print([a, b, c])
            print(int(a*b*c))
