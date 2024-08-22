from typing import List


class MedianOfTSA:
    def __init__(self, arr1: List[int], arr2: List[int]):
        self.arr1: List[int] = arr1
        self.arr2: List[int] = arr2

    def search_median(self) -> float:

        len_arr1, len_arr2 = len(self.arr1), len(self.arr2)

        if len_arr1 == 0:
            mid = len_arr2 // 2
            if len_arr2 % 2 == 0:
                return (self.arr2[mid] + self.arr2[mid - 1]) / 2
            return float(self.arr2[mid])

        if len_arr2 == 0:
            mid = len_arr1 // 2
            if len_arr1 % 2 == 0:
                return (self.arr1[mid] + self.arr1[mid - 1]) / 2
            return float(self.arr1[mid])

        if (len_arr1 + len_arr2) % 2 == 1:
            return float(search_median(self.arr1, self.arr2, 0, len_arr1-1, 0, len_arr2-1, (len_arr1 + len_arr2) // 2))

        med_low = search_median(self.arr1, self.arr2, 0, len_arr1-1, 0, len_arr2-1, (len_arr1 + len_arr2)//2 -1)
        med_high = search_median(self.arr1, self.arr2, 0, len_arr1-1, 0, len_arr2-1, (len_arr1 + len_arr2)//2)

        return (med_low + med_high) / 2


def search_median(arr1: List[int], arr2: List[int], l1: int, h1: int, l2: int, h2: int, k: int) -> int:

    if l1 == h1 and l2 == h2:
        cd1, cd2 = arr1[h1], arr2[h2]
        if h2 + h1 + 1 > k:
            return min(cd1, cd2)
        return max(cd1, cd2)
    if l1 == h1:
        if arr1[h1] > arr2[k - l1]:
            return arr2[k - l1]
        return max(arr2[k - l1 - 1], arr1[h1])

    if l2 == h2:
        if arr2[h2] > arr1[k - l2]:
            return arr1[k-l2]
        return max(arr1[k - l2 - 1], arr2[h2])

    mid1 = ((h1 + l1) // 2)
    mid2 = ((h2 + l2) // 2)

    if arr1[mid1] == arr2[mid2]:
        if k == (mid1 + mid2 + 1):
            return arr1[mid1]
        elif k < (mid1 + mid2 + 1):
            return search_median(arr1, arr2, l1, mid1, l2, mid2, k)
        else:
            return search_median(arr1, arr2, min(mid1+1, h1), h1, min(mid2+1, h2), h2, k)

    if arr1[mid1] > arr2[mid2]:
        if k == (mid1 + mid2 + 1):
            return search_median(arr1, arr2, l1, mid1, min(mid2+1, h2), h2, k)
        elif k < (mid1 + mid2 + 1):
            return search_median(arr1, arr2, l1, max(l1, mid1-1), l2, h2, k)
        else:
            return search_median(arr1, arr2, l1, h1, min(mid2+1, h2), h2, k)

    if k == (mid1 + mid2 + 1):
        return search_median(arr1, arr2, min(mid1+1, h1), h1, l2, mid2, k)
    elif k < (mid1 + mid2 + 1):
        return search_median(arr1, arr2, l1, h1, l2, max(l2, mid2-1), k)
    else:
        return search_median(arr1, arr2, min(mid1+1, h1), h1, l2, h2, k)


nums1 =[6,7]
nums2 = [1,2,3,4,5,8]

med_finder = MedianOfTSA(nums1, nums2)

print(med_finder.search_median())