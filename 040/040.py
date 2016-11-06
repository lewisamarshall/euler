from numpy import prod
nums = [str(i) for i in range(1,5000000)]
constant = ''.join(nums)
digit_list=[int(constant[i-1]) for i in [int(10**j) for j in range(0,7)]]
print constant[:1000]
print digit_list
print prod(digit_list)
