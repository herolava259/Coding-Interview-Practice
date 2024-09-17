

def maxSubarray(arr):
    maxSeq = arr[0]
    maxSA  = arr[0]
    maxConti = arr[0]

    for item in arr:
        tmp = maxConti+item

        if item > tmp:
            maxConti = item
        else:
            maxConti = tmp
        maxSA = max(maxConti,maxSA)

        if maxSeq < 0:
            maxSeq = max(item,maxSeq)
        else:
            maxSeq = max(item+maxSeq,maxSeq)

    return [maxSA,maxSeq]


arr = [-1,2,3,-4,5,10]

print(maxSubarray(arr))