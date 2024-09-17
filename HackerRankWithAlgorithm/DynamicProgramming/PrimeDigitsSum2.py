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
    return totalOfNDigits(n,number) in primes

def isTotallyDigitPrime(number):
    if number < 1000:
        return isPrimeOfLastDigit(3,number)
    if number < 10000:
        return isPrimeOfLastDigit(3, number // 10) and isPrimeOfLastDigit(3, number % 1000) and isPrimeOfLastDigit(4,number)

    first4 = number // 10
    last4 = number % 10000
    first3 = first4 // 10
    mid3 = last4 // 10
    last3 = last4 % 1000

    return isPrimeOfLastDigit(3, first3) and isPrimeOfLastDigit(3, mid3) and isPrimeOfLastDigit(3, last3) \
            and isPrimeOfLastDigit(4, first4) and isPrimeOfLastDigit(4, last4) and isPrimeOfLastDigit(5,number)

primesNumber3 = []
primesNumber4 = []
primesNumber5 = []

for item in range(100,1000):
    if(isPrimeOfLastDigit(3,item)):
        primesNumber3.append(item)

for item in range(1000,10000):
    if(isPrimeOfLastDigit(4,item)):
        primesNumber4.append(item)


for item in range(10000,100000):
    if(isPrimeOfLastDigit(5,item)):
        primesNumber5.append(item)


totalPrimes = defaultdict(int)

for item in primesNumber5:
    first4 = item//10
    last4 = item%10000
    first3 = first4//10
    mid3 = last4//10
    last3 = last4%1000
    check = isPrimeOfLastDigit(3,first3) and isPrimeOfLastDigit(3,mid3) and isPrimeOfLastDigit(3,last3) \
            and isPrimeOfLastDigit(4,first4) and isPrimeOfLastDigit(4,last4)
    if check:
        totalPrimes[item] += 1


perfectPrimes = list(totalPrimes.keys())

for i in range(100):
    if isPrimeOfLastDigit(2,i):
        perfectPrimes.append(i)

perfectPrimes.extend(primesNumber3)

for item in primesNumber4:
    if isPrimeOfLastDigit(3,item//10) and isPrimeOfLastDigit(3,item%1000):
        perfectPrimes.append(item)



total6Primes = defaultdict(int)

for key in totalPrimes.keys():
    newK  = (key%10000)*10
    for i in range(10):
        tmp = newK+i
        if isTotallyDigitPrime(tmp):
            total6Primes[tmp] +=1

sum = 0
for key in total6Primes.keys():
    sum += total6Primes[key]

def init():
    total5Primes = defaultdict(int)
    for item in range(10000,100000):
        if isTotallyDigitPrime(item):
            total5Primes[item] += 1
    return total5Primes

def primeDigitSums(n):
    totalCurrPrimes = init()
    totalNextPrimes = defaultdict(int)
    for i in range(5,n):
         totalNextPrimes.clear()
         for item in totalCurrPrimes.keys():
            tpl5 = (item%10000)*10
            for j in range(10):
                newK = tpl5 + j
                if isTotallyDigitPrime(newK):
                    totalNextPrimes[newK] = (totalNextPrimes[newK]+totalCurrPrimes[item])%MODK
         totalCurrPrimes.clear()
         totalCurrPrimes.update(totalNextPrimes)
    sum = 0
    for item in totalCurrPrimes.keys():
        sum = (sum+totalCurrPrimes[item])%MODK
    return sum

prefixToSuffixs = defaultdict(list)

for item in perfectPrimes:
    suffix = item%10000
    prefixToSuffixs[suffix].append(item)

nextToPrev = defaultdict(list)

for item in perfectPrimes:
    prefix = item//10
    nextToPrev[item].extend(prefixToSuffixs[prefix])

keys = list(nextToPrev.keys())

for key in keys:
    if len(nextToPrev[key]) == 0:
        nextToPrev.pop(key)
for key, value in nextToPrev.items():
    print(key, ": ", value)
print(len(nextToPrev.keys()))


def primeDigitSums2(n):
    totalCurrPrimes = init()

    for i in range(5,n):
        totalNextPrimes = defaultdict(int)
        for next,prevs in nextToPrev.items():
            sum = 0
            for prev in prevs:
                sum = (sum+totalCurrPrimes[prev])%MODK

            totalNextPrimes[next] = sum

        totalCurrPrimes.clear()
        totalCurrPrimes.update(totalNextPrimes)

    sums = 0
    for item in totalCurrPrimes.keys():
        sums = (sums + totalCurrPrimes[item]) % MODK
    return sums

print(primeDigitSums2(108222))





