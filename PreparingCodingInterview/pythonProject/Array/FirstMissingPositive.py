from typing import List


class FirstMissingPositiveSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:
        nums: List[int] = self.nums
        n = len(nums)

        for i in range(n):

            if nums[i] == i + 1:
                continue

            if nums[i] <= 0 or nums[i] >= n + 1:
                nums[i] = -(i + 1)
                continue

            idx = nums[i]
            nums[i] = -(i + 1)
            while 1 <= idx <= n and nums[idx - 1] != idx:
                swap_num = nums[idx - 1]
                nums[idx - 1] = idx
                idx = swap_num

        for num in nums:
            if num < 0:
                return -num

        return n + 1


nums1 = [3, 5, 2, 1]
sln = FirstMissingPositiveSolution(nums1)

print(sln.solve())
