from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[low]

    pos_left = low + 1
    pos_right = high

    while pos_left < pos_right:

        if arr[pos_left] > pivot >= arr[pos_right]:
            arr[pos_left], arr[pos_right] = arr[pos_right], arr[pos_left]
            pos_left += 1
            pos_right -= 1
        elif arr[pos_left] <= pivot:
            pos_left += 1
        elif arr[pos_right] > pivot:
            pos_right -= 1
        else:
            break

    arr[low], arr[pos_right-1] = arr[pos_right-1], arr[low]

    return pos_right-1


def quick_sort(arr: List[int], low: int, high: int):
    if low >= high:
        return
    pos_div = partition(arr, low, high)

    quick_sort(arr, low, pos_div - 1)
    quick_sort(arr, pos_div + 1, high)


arr1 = [3, 2, 5, 4, 7]

quick_sort(arr1, 0, len(arr1)-1)

print(arr1)
