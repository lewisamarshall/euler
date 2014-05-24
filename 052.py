def permute_test(n):
  for factor in range(2,7):
    multiple=n*factor
    if len(str(multiple)) != len(str(n)):
      return False
    for digit in str(n):
      if digit not in str(multiple):
        return False
  return True

n=0
while 1:
  n+=1
  if permute_test(n):
    break

print n
