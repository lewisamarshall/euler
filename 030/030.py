min=32
max=5000000

total=0
for i in range(min, max):
  dig_sum=0
  for ch in str(i):
    dig_sum+=int(ch)**5
  if i==dig_sum:
    print i
    total+=i

print total
