#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo which platform  """

Docsctring:

"""


import sys
print (sys.platform)

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)