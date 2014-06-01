data=open('words.txt').read().split(',')
words = [word.strip("\"").lower() for word in data]
print words[:10]
vals=[sum([ord(character)-96 for character in word]) for word in words]
print max(vals)

triangles = [a*(a+1)/2 for a  in range(30)]
print max(triangles)

total=0
for v in vals:
    if v in triangles:
        total +=1
print total
