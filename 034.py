from math import factorial

digit_factorials=[]

for i in range (10, int(1e7)):
  if i == sum(map(factorial, map(int, str(i)))):
    print i
    digit_factorials.append(i)

print sum(digit_factorials)
