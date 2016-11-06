import csv
import time
start_time = time.time()

tri = []
with open('triangle.txt') as inputfile:
    for row in csv.reader(inputfile, delimiter=' ', ):
        tri.append(map(int, row))

tri.reverse()
for idx, row in enumerate(tri):
    print idx
    if idx:
        for jdx, element in enumerate(row):
            tri[idx][jdx]+=max(tri[idx-1][jdx:jdx+2])
        print tri[idx]
print time.time() - start_time, "seconds"
