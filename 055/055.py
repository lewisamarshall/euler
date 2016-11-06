max=10000
total=0

def palindrome_test(i):
  for idx, char in enumerate(str(i)):
    if not char==str(i)[-(idx+1)]:
      return False
  return True

def lychrel_test(i):
  num_iter=0
  while num_iter<50:
    j=i+int(str(i)[::-1])
    if palindrome_test(j):
      return False
    else:
      i=j
      num_iter+=1
  return True

print lychrel_test(196)
print lychrel_test(47)

for i in range(1, max+1):
  if lychrel_test(i):
    print i
    total+=1

print total
