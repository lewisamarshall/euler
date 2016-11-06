def recip_test(d):
    n = 1
    numerators = []
    while True:
        if n == 0:
            return False
        elif n in numerators:
            return len(numerators)-numerators.index(n)
        elif n//d == 0:
            n *= 10
        else:
            numerators.append(n)
            n = n % d



recip_length = {d: recip_test(d) for d in range(2, 1000)}

longest_repeat = max(recip_length.values())
print recip_length.keys()[recip_length.values().index(longest_repeat)], longest_repeat
