from typing import List


class PeakIndexSolution:
    def __init__(self, arr: List[int]):

        self.arr: List[int] = arr

    def solve(self) -> int:

        n = len(self.arr)
        low, high = 0, n - 1

        while low < high:

            mid = (low + high) >> 1

            left_val = self.arr[mid - 1] if mid > 0 else -1
            right_val = self.arr[mid + 1] if mid < n - 1 else 10 ** 6 + 1
            cur_val = self.arr[mid]

            if left_val < cur_val < right_val:
                low = mid + 1
            elif left_val > cur_val > right_val:
                high = mid - 1
            elif left_val < cur_val > right_val:
                return mid
            else:
                break

        if low < 0:
            return 0
        if low >= n:
            return n - 1

        return low


arr1 = [0, 9, 10, 5, 2]

sln = PeakIndexSolution(arr1)

print(sln.solve())
