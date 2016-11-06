max=1000000

from isprime import isprime

def rotation(i, n):
  i=str(i)
  return int(i[n:]+i[:n])

def circular_prime(i):
  for idx in range(len(str(i))):
    if not isprime(rotation(i,idx)):
      return False
  return True

circulars=[]
for i in range(max+1):
  if circular_prime(i):
    circulars.append(i)

print len(circulars)
print circulars
