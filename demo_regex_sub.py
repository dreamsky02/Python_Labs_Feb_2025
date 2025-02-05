#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""

#Sample line from /etc/passwd on Linux for the root user login

line ="root:x:0:0: The Super User:/root:/bin/ksh"

line =re.subn(r"[Ss]uper [Uu]ser", r"Administrator", line)
(line,num) = re.subn(r"ksh$", r"bash", line)


print(f"Modified line = {line}")
