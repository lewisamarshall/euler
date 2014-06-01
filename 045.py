def triangle(n):
    return n*(n+1)/2


def pentagonal(n):
    return n*(3*n-1)/2


def hexagonal(n):
    return n*(2*n-1)


triangles = [triangle(n) for n in range(286, 55400)]
pentagons = [pentagonal(n) for n in range(166, 32000)]
hexagons = [hexagonal(n) for n in range(144, 27800)]

for k in triangles:
    if k in pentagons and k in hexagons:
        print k, triangles.index(k), pentagons.index(k), hexagons.index(k)
        break
