import numpy
n=3
spiral = [[None] * n for i in range(n)]

spiral=numpy.array(spiral)
location=[0,0]
direction=0

for i in reversed(range(1,n**2+1)):
    spiral[location[0]][location[1]]=i
    print spiral
    print location
    if direction==0:
        if not location[0]==n-1 and not spiral[location[0]-1][location[1]]:
          location[0]+=1
        else:
          direction+=1
          location[1]+=1
    elif direction==1:
        if not location[1]==n-1 and not spiral[location[0], location[1]+1]:
          location[1]+=1
        else:
          direction+=1
          location[0]-=1
    elif direction==2:
        if not location[0]==0 and not spiral[location[0]-1][location[1]]:
          location[0]-=1
        else:
          direction+=1
          location[1]-=1
    elif direction==3:
        if not location[1]==0 and not spiral[location[0]][location[1]-1]:
          location[1]-=1
        else:
          direction=0
          location[1]+=1

# print spiral
# total=0
# for i in range(n):
#   total+=spiral[i,i]+spiral[-i,-i]
# if n%2==1:
#   total-=spiral[n/2-0.5, n/2-0.5]
#
# print total
