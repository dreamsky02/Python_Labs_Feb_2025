#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
"""

Docsctring:

"""
import sys
import re

if sys.platform == "win32":
    filename = r"c:\windows\system32\drivers\etc\services"
else:
    filename: r"/etc/serv ices"

all_ports = set (range (1,201))
used_ports = set()
with open(filename, mode="rt") as fh_service:
    for line in fh_service:
        m = re.search(r"(\d+)/(tcp|udp)" , line)
        if m:
            port = int(m.group(1))
            if port <=200:
                used_ports.add(port)

print (f"All ports = {all_ports}")
print (f"Used ports = {used_ports}")
print(f"Unused ports = {all_ports - used_ports}")

