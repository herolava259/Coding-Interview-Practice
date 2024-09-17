def gcd(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp

    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * (b // gcd(a, b))


def gcd_group(a):
    if len(a) < 2:
        return a[0]
    res = a[0]
    for item in a[1:]:
        res = gcd(res, item)
    return res


def lcm_group(a):
    if len(a) < 2:
        return a[0]
    x = a[0]
    y = a[1]
    res = lcm(x, y)
    for item in a[2:]:
        res = lcm(res, item)
    return res


def getTotalX(a, b):
    # Write your code here
    minFactor = lcm_group(a)
    maxMultiple = gcd_group(b)
    i = 1
    counter = 0
    gap = maxMultiple // minFactor

    while i <= gap:
        if gap % i == 0:
            counter += 1
        i+=1

    return counter

a = [2,4]
b = [16,32,96]

print(getTotalX(a,b))