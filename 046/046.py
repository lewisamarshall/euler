from isprime import isprime
from math import sqrt

primes=[]

def goldbach2(i,lesser_primes):
  if isprime(i):
    return True
  else:
    for j in lesser_primes:
      base=sqrt((i-j)/2)
      if base==int(base):
        return True
  return False

flag=True
i=1
while flag:
  i+=1
  if isprime(i):
    primes.append(i)
    flag=True
  else:
    flag=goldbach2(i, primes)

print i
