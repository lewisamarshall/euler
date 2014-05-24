from seive import eratosthenes as sieve
from factors import factorize_quick as factors

max=10000000
primes=sieve(max)

print(len(primes))

def totient(n, primes):
  n_factors=factors(n, primes)
  for i in range(1, n):
