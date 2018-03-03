import random
print("Number from 0 to 1000 ")
randomNumber = {}
for i in range(0, 100):
    randomNumber[i] = random.randint(0, 1000)
    if randomNumber[i] % 2 == 0:
        print(randomNumber[i])
    else:
        continue