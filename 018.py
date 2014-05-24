import csv
import time
tic=time.clock()
tri = []
with open('018.dlm') as inputfile:
    for row in csv.reader(inputfile, delimiter=' ', ):
        tri.append(map(int, row))

print tri
tri.reverse()
for idx, row in enumerate(tri):
    print idx
    if idx:
        for jdx, element in enumerate(row):
            tri[idx][jdx]+=max(tri[idx-1][jdx:jdx+2])
        print tri[idx]
toc=time.clock()
print (toc-tic)*1000
#for list in
