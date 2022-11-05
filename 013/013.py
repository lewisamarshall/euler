import numpy

a = numpy.genfromtxt('013.dlm', dtype=float)
print(a)
print(len(a))
print(int(sum(a)/10**42))
