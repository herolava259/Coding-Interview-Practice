import os
from collections import defaultdict


primes = [2,3,5,7,11,13,17,19,23,29,31,37,39,41,43]
MODK = 10**9+7

def totalOfNDigits(n, number):
    sum = 0
    while n > 0:
        sum += number%10
        number = number // 10
        n -= 1

    return sum


def isPrimeOfLastDigit(n, number):
    return totalOfNDigits(n, number) in primes


def isTotallyDigitPrime(number):
    if number < 1000:
        return isPrimeOfLastDigit(3, number)
    if number < 10000:
        return isPrimeOfLastDigit(3, number // 10) and isPrimeOfLastDigit(3, number % 1000) and isPrimeOfLastDigit(4,
                                                                                                                   number)

    first4 = number // 10
    last4 = number % 10000
    first3 = first4 // 10
    mid3 = last4 // 10
    last3 = last4 % 1000

    return isPrimeOfLastDigit(3, first3) and isPrimeOfLastDigit(3, mid3) and isPrimeOfLastDigit(3, last3) \
           and isPrimeOfLastDigit(4, first4) and isPrimeOfLastDigit(4, last4) and isPrimeOfLastDigit(5, number)


#
# Complete the 'primeDigitSums' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def init():
    total5Primes = defaultdict(int)
    for item in range(10000, 100000):
        if isTotallyDigitPrime(item):
            total5Primes[item] += 1
    return total5Primes


perfectPrimes = []
for i in range(2, 100000):
    if isTotallyDigitPrime(i):
        perfectPrimes.append(i)
prefixToSuffixs = defaultdict(list)

for item in perfectPrimes:
    suffix = item % 10000
    prefixToSuffixs[suffix].append(item)



nextToPrev = defaultdict(list)

for item in perfectPrimes:
    prefix = item // 10
    nextToPrev[item].extend(prefixToSuffixs[prefix])

keys = list(nextToPrev.keys())

for key in keys:
    if len(nextToPrev[key]) == 0:
        nextToPrev.pop(key)

# for key, value in nextToPrev.items():
#     print(key, ": ", value)
# print(len(nextToPrev.keys()))

primeSums = [0, 0, 0, 0, 0, 0]
totalCurrPrimes = init()


def primeDigitSums(n):
    if len(primeSums) >= n + 1:
        return primeSums[n]

    m = len(primeSums)

    for i in range(m, n + 1):
        totalNextPrimes = defaultdict(int)
        for next, prevs in nextToPrev.items():
            sum = 0
            for prev in prevs:
                sum = (sum + totalCurrPrimes[prev]) % MODK

            totalNextPrimes[next] = sum

        totalCurrPrimes.clear()
        totalCurrPrimes.update(totalNextPrimes)
        sums = 0
        for item in totalCurrPrimes.keys():
            sums = (sums + totalCurrPrimes[item]) % MODK
        primeSums.append(sums)
    return primeSums[n]


for item in totalCurrPrimes:
    print(item)

print(len(totalCurrPrimes.keys()))