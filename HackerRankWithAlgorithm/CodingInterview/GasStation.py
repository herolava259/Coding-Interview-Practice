

def gas_station(gas, cost):
    remainders = [g-c for g,c in zip(gas,cost)]
    start = 0
    remain = 0
    prev_remaining = 0
    for i, item in enumerate(remainders):
        remain += item
        if remain < 0:
            start = i+1
            prev_remaining += remain
            remain = 0


    if start == len(remainders) or remain + prev_remaining < 0:
        return -1

    return start
gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
print(gas_station(gas,cost))
