def ispal(x):
    x = str(x)
    for i in range(len(x)):
        if not x[i-1] == x[-i]:
            return False
    return True

greatest = 0;
for i in range(999, 100, -1):
    for j in range(999, i, -1):
        product = i*j
        if product > greatest:
            if ispal(product):
                greatest = product
        else:
            break

print(greatest)
