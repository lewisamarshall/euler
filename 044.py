max=10000

pentagons=[]
sum_pentagons=[]
n=0
while 1:
  current_pentagon=n*(3*n-1)/2
  pentagons.append(current_pentagon)
  for i in pentagons:
    if current_pentagon-i in pentagons:
      sum_pentagons.append(current_pentagon)
      if i in sum_pentagons:
        print current_pentagon, i
        break
