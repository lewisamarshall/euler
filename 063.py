total = 0
for power in range(1, 25):
    for digit in range(1, 10):
        value = len(str(digit**power))
        if value == power:
            print digit, power, digit**power
            total += 1
print(total)
