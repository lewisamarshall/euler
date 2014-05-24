summation = 0
for i in range(1, 101):
    summation += i**2
print abs(summation-sum(range(1, 101))**2)
