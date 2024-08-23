from typing import List


class MaximumAverageSubArrayISolution:

    def __init__(self, nums: List[int], k: int):

        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> float:

        sum_cur_k = sum(self.nums[:self.k])
        max_sum = sum_cur_k
        if self.k == len(self.nums):
            return sum_cur_k / self.k
        for i in range(1, len(self.nums) - self.k + 1):
            sum_cur_k += self.nums[i + self.k - 1] - self.nums[i-1]
            if sum_cur_k > max_sum:
                max_sum = sum_cur_k

        return max_sum / self.k


nums1 = [0,1,1,3,3]
k1 = 4

sln = MaximumAverageSubArrayISolution(nums1, k1)

print(sln.solve())
