
def insertionSort1(n, arr):
    # Write your code here
    compare = arr[-1]
    isChanged = False
    for i in range(n -2 ,-1 ,-1):
        if arr[i] > compare:
            arr[i+1] = arr[i]
            isChanged = True
        else:
            if arr[i+1] == compare:
                isChanged = False
            else:
                arr[i+1] = compare
            compare = arr[i]
        if isChanged:
            print(*arr)

    if arr[0] > compare:
        arr[0] = compare
        print(*arr)



n = 10
arr = [int(item) for item in "2 3 4 5 6 7 8 9 10 1".split(' ')]

insertionSort1(10,arr)