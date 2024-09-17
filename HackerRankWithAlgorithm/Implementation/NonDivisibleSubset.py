

def nonDivisibleSubset(k, s):
    # Write your code here


    sizeOfMods = [0 for i in range(k)]

    for item in s:
        sizeOfMods[item % k] += 1
    if sizeOfMods[0] > 0:
        sizeOfMods[0] = 1
    half_k = -1
    if k % 2 == 0:
        half_k = k // 2
        if sizeOfMods[half_k] > 0:
            sizeOfMods[half_k] = 1

    sizeOfMods = [(i, sizeOfMods[i]) for i in range(k)]

    sizeOfMods.sort(key=lambda x: x[1], reverse=True)

    choose = []
    maxS = 0
    for pair in sizeOfMods:
        if (k-pair[0]) % k not in choose:
            maxS += pair[1]
            choose.append(pair[0])

    return maxS

s = [19,10,12,10,24,25,22]
k = 4

print(nonDivisibleSubset(k,s))






