

#Descritption: This Script will generate 6 RANDOM lottery numbers.

import random


lotto = []

while len(lotto) < 6:
    num = random.randint(1,50)
    lotto.append(num)
    if num not in lotto:
        lotto.append(num)
    else:
        print ("Duplicate number =", num)

print ("Lottery number=" , lotto)
print ("Lottery number=" , lotto)


