from fractions import Fraction

rationals = [Fraction(i*3//7, i) for i in range(1, 1000000) if not i % 7 == 0]
rationals = set(rationals)
print max(rationals)
