#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
"""

Docsctring:

"""


master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN:")
    if pin == master_pin:
        print ("Valid PIN")

    else:
        print ("Invalid PIN")
        attempts +=1

else:
    print ("Too many attempts")
    print ("Your card has been retained. Have a nice day!")


print("Done.")

