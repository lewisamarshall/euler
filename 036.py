from palindromes import palindrome_test

total = 0

for i in range(1, 1000000):
    if palindrome_test(i) and palindrome_test(str(bin(i))[2:]):
        total += i

print total
