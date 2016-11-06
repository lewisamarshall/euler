from fractions import Fraction

rationals=[]
for i in range(1,1000):
    rationals += [Fraction(j,i) for j in range(1,i)]
rationals = set(rationals)
print len(rationals)
