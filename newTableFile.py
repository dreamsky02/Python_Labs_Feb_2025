#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""
Docsctring:

"""

for pos in range(0,65536):
    try:
    print(pos, chr(pos), end ="")
    if pos % 16 == 0:
        print()
    except UnicodeError:
    print("", end=" ")

