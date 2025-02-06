#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""
def get_numbers():
    numbers = []
    for x in range (0,100):
        numbers.append(x)
    return numbers

def generate_numbers():

    for x in range(0, 10):
        yield x

for z in generate_numbers():
    print(z)

#Using a while loop

gen = generate_numbers()
while True:
    num =next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

gen = get_numbers()
num1 = next(gen, False)
num2 = next(gen)
num3 = next(gen)
print(num1,num2, num3)