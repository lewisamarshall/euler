from factors import *

def abundance_test(n):
    """Returns -1 if n is deficient, 0 if n is perfect, and 1 if n is abundant."""
    div_sum=sum(proper_divisors(n))
    return cmp(div_sum, n)

abundants=[]
summation=0
for i in range(1,28123):
    writable=False
    if abundance_test(i)==1:
        abundants.append(i)
    for ab in abundants:
        if (i-ab) in abundants:
            writable=True
            break
    if not writable:
        summation+=i

print summation

#print len(abundants)
#print abundants[-1]

#summation=0
#for i in range(1, 100):
#    print i
#    for ab in abundants:
#        if not (i-ab) in abundants:
#            summation+=i

#print i
#364327
