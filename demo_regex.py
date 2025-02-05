#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""
#open file handle for reading in text mode

import re

fh_in=open(r"c:\labs\words", mode="rt")

#Iterate through file handle one line at a time
for line in fh_in:
    #Example of str testing = GOOD
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    #print(line, end="")
    #m = re.search("ing$", line)
    # m = re.search("^ringing$", line)

    m = re.search("^ringing$", line)
    if m:
        print(line, end="")

