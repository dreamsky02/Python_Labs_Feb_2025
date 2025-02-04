#! /usr/bin/env Python 3
# Author: EMares
# Description: This script will demo
#
#
#
"""

Docsctring:

"""
planets = {'Mercury': 57.91,
           'venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94}

for planet in planets.keys():
    print("\t\t" + planet +": " + str (planets[planet])+ " Gm\t" +str(hex(0xff)))


print("-" *60 )

for planet in planets.keys():
    print("{0:>12s} {1:>12.3f} GM {2:#6o} ".format(planet, planets[planet], 0xff))

for planet in planets.keys():
    print("{planet:>12s} {planets[planet]:>12.3f} GM {2:#6o} ".format(planet, planets[planet], 0xff))





