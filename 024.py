import itertools

digits=[]
for i in range(10):
  digits.append(str(i))

for idx, perm in enumerate(itertools.permutations(range(10),10)):
  if idx==1000000-1:
    print perm
