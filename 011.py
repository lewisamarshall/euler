import csv
import numpy

a = numpy.genfromtxt('011.dlm', dtype=int)
print a


from numpy import prod

product=1
for i, row in enumerate(a):
    for j, column in enumerate(row):
        if numpy.prod(a[i:i+4, j]) > product:
            print a[i:i+4, j]
            product = numpy.prod(a[i:i+4, j])
        if numpy.prod(a[i, j:j+4]) > product:
            print a[i, j:j+4]
            product = numpy.prod(a[i, j:j+4])
        try:
            if numpy.prod([a[i, j], a[i+1, j+1], a[i+2, j+2], a[i+3, j+3]]) > product:
                print([a[i, j], a[i+1, j+1], a[i+2, j+2], a[i+3, j+3]])
                product = numpy.prod([a[i, j], a[i+1, j+1], a[i+2, j+2], a[i+3, j+3]])
        except:
            False
        try:
            if numpy.prod([a[i, j], a[i+1, j-1], a[i+2, j-2], a[i+3, j-3]]) > product:
                print([a[i, j], a[i+1, j-1], a[i+2, j-2], a[i+3, j-3]])
                product = numpy.prod([a[i, j], a[i+1, j-1], a[i+2, j-2], a[i+3, j-3]])
        except:
            False


print(product)
