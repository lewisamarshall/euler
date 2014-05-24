longest_repeat=0
num=1
for d in range(1,11):
    print d
    repeat=1
    while  (10**repeat%d and (10**repeat-1)%d):
        repeat+=1
    if repeat>longest_repeat:
        longest_repeat=repeat
        num=d
    print d, repeat

print(longest_repeat, num)
