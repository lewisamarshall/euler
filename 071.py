from fractions import Fraction

rationals = set{Fraction(i*3//7,i) for i in range(1,10000) if isreduced(i*)}
print rationals[:10]
# print max([i for i in rationals if i ! Fraction(3/7)])
