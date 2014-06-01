coins = [200, 100, 50, 20, 10, 5, 2, 1]

target = 200
ways=0
for duce in range(2):
    for single in range(3):
        for fify in range(5):
            for twenty in range(11):
                for dime in range(21):
                    for nickle in range(41):
                        for twopence in range(101):
                            for penny in range(201):
                                total = penny+2*twopence+nickle*5+dime*10+twenty*20+fify*50+single*100+duce*200
                                if total==target:
                                    ways +=1

print ways
