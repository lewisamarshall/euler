import numpy
import time
a=time.time()
domain = 51
total = 0
for x1 in range(domain):
    for y1 in range(domain):
        vec1 = [x1, y1]
        for x2 in range(domain):
            for y2 in range(domain):
                vec2 = [x2, y2]
                vec3 = [x2-x1, y2-y1]
                if vec1 != vec2 and vec2 != vec3 and vec1 != [0, 0] and vec2 != [0, 0]:
                    if not numpy.dot(vec1, vec2) or not numpy.dot(vec1, vec3) or not numpy.dot(vec2, vec3):
                        total += 1
                        # print vec1, vec2

print total/2
print time.time()-a
