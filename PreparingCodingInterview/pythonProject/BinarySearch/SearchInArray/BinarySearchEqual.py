from typing import List


class BinarySearchSolution:
    def __init__(self, nums: List[int], target: int):
        self.nums: List[int] = nums
        self.target: int = target

    def solve(self) -> int:
        n = len(self.nums)

        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2
            mid_val = self.nums[mid]

            if mid_val == self.target:
                return mid
            elif mid_val > self.target:
                high = mid
            else:
                low = mid+1

        return low if self.nums[low] == self.target else -1


nums1 = [-1,0,3,5,9,12]
target1 = 2

sln = BinarySearchSolution(nums1, target1)

print(sln.solve())
