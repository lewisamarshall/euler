from num2words import num2words
letters=0
for i in range(1, 1001):
    numstr=num2words(i)
    numstr=numstr.replace(" ", "")
    numstr=numstr.replace("-", "")
    letters+=len(numstr)
    print numstr
print letters
    