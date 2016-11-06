import csv
import string
from math import log

data=[]
datafile = open('base_exp.txt')
reader = csv.reader(datafile)
for row in reader:
  data.append(map(int, row))

max_line=0
for idx, pair in enumerate(data):
  if pair[1]*log(pair[0])>data[max_line][1]*log(data[max_line][0]):
    max_line=idx

print max_line+1, data[max_line]
