#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""



import re

fh_in=open(r"c:\labs\words", mode="rt")

#Iterate through file handle one line at a time
for line in fh_in:
    #Example of str testing = GOOD
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    #print(line, end="")
    #m = re.search(r"ing$", line)
    # m = re.search(r"^ringing$", line)
    #  m = re.search(r"^.ringing$", line)
    # m = re.search(r"^................ringing$", line)
    #m = re.search(r"[adr]ing$", line)
    #m = re.search(r"^[A-Z]]", line)
    #m = re.search(r"\.", line)
    #m = re.fullmatch(r"^[A-Z].{4}[A-Z]\n$", line)
    #m = re.search(r"^(.)(.).\2\1$",line)

for line in fh_in:
    #re.compile(r"^([A-Z]).*\1$")
    m = reobj.search(line)
    if m:
        print(line, end="")

