

#  1 2 3 4

def fairCut(n,k,arr):
    if n-k < k:
        k = n-k

    arr.sort()

    isevenn = n % 2 == 0
    isevenk = k % 2 == 0

    indices = []

    if (isevenn and isevenk ) or (not isevenn and isevenk):

        x = (n+1) // 2

        for i in range(k//2):
            indices.append(x - (2*i+1))
            indices.append(x + (2*i+1))

    if (isevenn and not isevenk) or (not isevenn and not isevenk):
        x = (n+1) // 2
        indices = [x]
        for i in range(k//2):
            indices.append(x - (2*(i+1)))
            indices.append(x + (2*(i+1)))

    s1 = []
    s2 = []

    for i in range(0,n):
        if i + 1 in indices:
            s1.append(arr[i])
        else:
            s2.append(arr[i])

    sum = 0
    for i in s1:
        for j in s2:
            sum += abs(i-j)

    return sum

arr = [1,2,3,4]
n = 4
k = 2

print(fairCut(n,k,arr))