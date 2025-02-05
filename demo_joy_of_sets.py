#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo """Docsctring:

""" """
marvel_fans= {'eliza', 'liz', 'lizzy','lizbeth'}
dc_fans = set ()

dc_fans.add('mark')
dc_fans.add('donald')
dc_fans.add('mathew')

dc_fans.pop()

print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")