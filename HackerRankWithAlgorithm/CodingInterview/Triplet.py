arr = [12, 3, 4, 1, 6, 9]
k = 24


def triplet(arr, k):
    for a in arr:
        for b in arr:
            for c in arr:
                if a + b + c == k:
                    return (a, b, c)

    return (-1, -1, -1)


def triplet2(arr, k):
    arr.sort()
    # 1,3,4,6,9,12
    # 24
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for l in range(i + 2, n):
                if arr[i] + arr[j] + arr[l] == k:
                    return (arr[i], arr[j], arr[l])

    return (-1, -1, -1)


def binary_search(arr, low, high, a):
    first = low
    last = high

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            last = mid - 1
        else:
            first = mid + 1

    return -1


def triplet3(arr, k):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            l = binary_search(arr, j + 1, n - 1)
            if l >= 0:
                return True
            if arr[i] + arr[j] + arr[j + 1] > k:
                return False
    return False

def doublet(arr,low,high, k):

    for i in range(low,high+1):
        if k - arr[i] > k//2:
            return False
        j = binary_search(arr,i+1,len(arr)-1,k-arr[i])
        if j >=0:
            return True
    return False

def triplet4(arr, k):
    arr.sort()
    for i in range(len(arr)-2):
        if doublet(arr,i+1,len(arr)-2,k-arr[i]):
            return True
    return False


arr.sort()
#1,3,4,6,9,12
print(binary_search(arr,0,len(arr)-1,1))