def partition(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1
    while True:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left >= right:
            break
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        left += 1
        right -= 1

    arr[high] = arr[left]
    arr[left] = pivot
    return left


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


arr = [4, 5, 3, 7, 2]
quickSort(arr, 0, 4)

print(arr)
