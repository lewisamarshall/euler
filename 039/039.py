from math import sqrt
import matplotlib.pyplot as plt
from numpy import histogram as hist
triangles={}
lengths=[]

for a in range(1,1000):
  for b in range(1,a+1):
    c=sqrt(a**2+b**2)
    perim=int(a+b+c)
    if c==int(c) and perim <=1000:
      lengths.append(perim)
      if perim in triangles:
         triangles[perim]+=1
      else:
         triangles[perim]=1

print max(triangles, key=triangles.get)
plt.plot(triangles.keys(), triangles.values(), 'o')
plt.show()
