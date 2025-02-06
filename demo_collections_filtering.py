#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:How to copy and optionally filter source collection to a destination collection using different methods.

"""
from ctypes.wintypes import SHORT

students = ['euler','jorge','mark','elizabeth','jeremy','erik','javon','kirill']

wee_names= []
for name in students:
    if len(name) <=5:
        wee_names.append(name)

print("f@Short names = {wee_names}")

def filter_names(name):
    if len(name) <= 5:
        return True
    else:
        return False
wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name)
print(f"2.Short names = {wee_names}")

wee_names = list(filter (lambda name:len(name) <=5, students))
print(f"3.Short names = {wee_names}")

