def digit_sum(n):
    return sum((int(x) for x in str(n)))
    
print digit_sum(2**1000)