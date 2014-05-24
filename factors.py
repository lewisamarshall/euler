def factorize_quick(n, primes):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))

    return factors
    
def factorize(n):
    factors=[]
    for i in range(2, int(n**.5)):
        j=0
        while n%i==0:
            n//=i
            j+=1
        if j>0:
            factors.append((i,j));
    if n>1: factors.append((n,1))
    
    return factors
    
def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div
    
def proper_divisors(n):
    divs=divisors(factorize(n))
    return divs[:-1]