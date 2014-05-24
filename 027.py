from isprime import isprime

best=(0,0)
nmax=0
for a in range(-999,1000):
  for b in range(-999,1000):
    n=0
    while isprime(n**2+a*n+b):
      n+=1
    if n > nmax:
      nmax=n
      best=(a,b)
      print 'new n is', n
      print 'new pair is', best
print 'best n is', nmax
print 'best pair is', best
print 'best product is', best[0]*best[1]
