import csv
data=[]
with open('names.txt') as inputfile:
    for row in csv.reader(inputfile, delimiter=','):
       data=row
print data[0:10]


data=sorted(data)


total=0
for idx, name in enumerate(data):
    namescore=0
    for letter in name:
        namescore+=ord(letter)-ord("A")+1
    total+=(idx+1)*namescore
    
print total