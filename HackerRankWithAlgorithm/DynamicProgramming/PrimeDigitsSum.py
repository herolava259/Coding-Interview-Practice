import math
import os
import random
import re
import sys
from collections import defaultdict

primes = [2,3,5,7,11,13,17,19,23,29,31,37,39,41,43]
MODK = 10**9+7
def sumlastNdigit(n, num):
    sum = 0
    i = 0
    while i < num and n >0:
        sum += n%10
        n = n//10
        i += 1
    return sum

# print(sumlastNdigit(123456,3))

patterns = []




def init(dicts):
    for item in range(100,1000):
        if sumlastNdigit(item,3) in primes:
            patterns.append(item)

    for item in range(1000,10000):
        if sumlastNdigit(item,4) in primes:
            patterns.append(item)

    for item in range(10000,100000):
        if sumlastNdigit(item,5) in primes:
            patterns.append(item)
            if sumlastNdigit(item,4) in primes and \
                    sumlastNdigit(item//10,4) in primes and \
                    sumlastNdigit(item,3) in primes and \
                    sumlastNdigit(item//10,3) in primes and \
                    sumlastNdigit(item//10//10,3) in primes :

                dicts[item] +=1

# for item in dicts.keys():
#     print(item)

def checkTailIsPrime(n):

    return sumlastNdigit(n,5) in primes and sumlastNdigit(n,4) in primes and sumlastNdigit(n,3) in primes

def primeDigitSums(n):
    new_dicts = defaultdict(int)
    dicts = defaultdict(int)
    init(dicts)
    #tmp_dicts = dicts.copy()
    for idx in range(6,n):
        new_dicts.clear()

        for item in dicts.keys():
            num = dicts[item]

            for i in range(9):
                n_item = (item%1000)*10 + i
                if checkTailIsPrime(n_item):
                    new_dicts[n_item] = (new_dicts[n_item]+num)%MODK
        dicts = new_dicts.copy()

    sum = 0

    for key in dicts.keys():
        print(key)
        sum = (sum + dicts[key])

    return len(dicts.keys())

print(primeDigitSums(6))














