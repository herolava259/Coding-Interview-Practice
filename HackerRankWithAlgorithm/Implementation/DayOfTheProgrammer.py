#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here

    totalDayOfEveryMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    isLeapYear = False

    if year > 1918:
        if year % 400 == 0:
            isLeapYear = True
        elif year % 4 == 0 and year % 100 != 0:
            isLeapYear = True

    elif year < 1918:
        if year % 4 == 0:
            isLeapYear = True
    daySt = 256
    if isLeapYear:
        daySt -= 1

    if year != 1918:
        month = 1
        while month <= 12 and daySt > totalDayOfEveryMonth[month - 1]:
            daySt -= totalDayOfEveryMonth[month - 1]
            month += 1
    else:
        month = 3
        daySt -= 31
        daySt -= 15
        while month <= 12 and daySt > totalDayOfEveryMonth[month - 1]:
            daySt -= totalDayOfEveryMonth[month - 1]
            month += 1

    date = ''
    if month < 10:
        date += str(daySt)
        date += '.'
        date += '0'
        date += str(month)
        date += '.'
        date += str(year)
    else:
        date += str(daySt)
        date += '.'
        date += str(month)
        date += '.'
        date += str(year)

    return date


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
