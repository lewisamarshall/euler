from factors import factorize, divisors

def amicable_test(k):
    compliment=sum(divisors(factorize(k))[:-1])
    if sum(divisors(factorize(compliment))[:-1])==k:
        print k, compliment
    return sum(divisors(factorize(compliment))[:-1])==k and not k==compliment
    
print amicable_test(220)
print(divisors(factorize(220)))[:-1]

amicable=[]
for n in range(2,10000):
    if amicable_test(n):
        amicable.append(n)
        
print amicable
print sum(amicable)
    