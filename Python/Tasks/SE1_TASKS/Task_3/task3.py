#!/usr/bin/python3

import calendar

y = int(input("Enter a year: "))
m = int(input("Enter a month: "))

month = calendar.month(y,m)

print(month)