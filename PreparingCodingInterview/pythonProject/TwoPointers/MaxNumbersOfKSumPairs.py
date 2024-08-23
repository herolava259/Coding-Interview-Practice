from typing import List


class MaxNumberOfKSumPairsSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> int:

        self.nums.sort()

        first_p, last_p = 0, len(self.nums) - 1
        num_equal_k = 0
        while first_p < last_p:
            total_val = self.nums[first_p] + self.nums[last_p]
            if total_val < self.k:
                first_p += 1
            elif total_val > self.k:
                last_p -= 1
            else:
                num_equal_k += 1
                first_p += 1
                last_p -= 1
        return num_equal_k


nums1 = [1, 2, 3, 4]
k1 = 5

sln = MaxNumberOfKSumPairsSolution(nums1, k1)

print(sln.solve())