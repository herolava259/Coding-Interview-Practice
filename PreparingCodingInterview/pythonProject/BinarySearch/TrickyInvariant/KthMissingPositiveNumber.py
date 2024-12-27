from typing import List


class FindingKthPositiveSolution:
    def __init__(self, arr: List[int], k: int):
        self.arr: List[int] = arr
        self.k: int = k

    def solve(self) -> int:

        low, high = 0, len(self.arr) - 1

        while low < high:
            mid = ((low + high) >> 1) + ((low + high) & 1)

            cur_val = self.arr[mid]

            num_missing = cur_val - mid - 1

            if num_missing > self.k:
                high = mid - 1
            else:
                low = mid

        num_missing = self.arr[low] - low - 1

        if low == 0 and self.arr[low] > self.k:
            return self.k

        if num_missing < self.k:
            return self.arr[low] + self.k - num_missing

        while low > 0 and self.arr[low] == self.arr[low - 1] + 1:
            low -= 1
        return self.arr[low] - 1


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sln = FindingKthPositiveSolution(arr, k)

        return sln.solve()