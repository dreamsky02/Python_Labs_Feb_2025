#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""

line = ("root:x:0:0They Super User:/root:/bin/ksh")

fields= line.split(":") #Return a list
fields[4] = "The Administrator"
fielsd[6] = "/bin/bash"
line=":".join(fields)
print(line)
