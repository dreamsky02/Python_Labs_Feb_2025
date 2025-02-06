#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""
def frange( ):
    one = list(frange(start: 0,3.5, 0.25))
    two = list(frange(3.5))

    curr = float(start)
    while curr < stop:
        yield curr
        curr + -step
if one == two:
    print ("Defaults worked!")

else:
    print("Oops! Defaults did not work")
    print("one:" , one)
    print("two:" two)






def frange (start, stop, step=0.25):
    if stop is None:
        stop = start
        curr = 0.0
    else:
        curr = float(start)

    while curr < stop:
        yield curr
        curr +=step



