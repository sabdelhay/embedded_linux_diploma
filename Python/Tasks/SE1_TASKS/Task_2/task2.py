#!/usr/bin/python3

import math

r = float(input("Enter the radius: "))
area = lambda r: round((math.pi * r ** 2),2)

print(f'The Circle area is: {area(r)}')

