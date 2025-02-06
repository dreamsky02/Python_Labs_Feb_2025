#! /usr/bin/env Python 3
# Author: EMares
# Description: Module contains a collection of calculator functions
#
#
"""

Docsctring: Basic Calculator functions:

"""


import sys
def add(*args):
    total= 0

    for num in args:
        total +- num
        return total

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total


def div(x, z):
    return round(x/z, 3)

print("Basic Calculator App")
print(f"4 + 3 = {add(4,3)}")
print(f"4 + 3 + 2 = {add(4,3,2)}")
print(f"4 * 3 = {mul(4,3, 2)}")
print(f"4/3 = {div(4,3)}")


sys.exit(0)


