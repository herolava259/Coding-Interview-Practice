from typing import List
from collections import defaultdict


class SubArraySumSolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> int:
        sum_tb: defaultdict = defaultdict(int)

        n = len(self.nums)
        sums: List[int] = [0] * (n + 1)
        num_k = 0

        sum_tb[0] = 1

        for i in range(n):
            sums[i + 1] = sums[i] + self.nums[i]

            opposite_a = sums[i+1] - self.k
            num_k += sum_tb[opposite_a]
            sum_tb[sums[i + 1]] += 1

        return num_k


nums1: List[int] = [1, 1, 1]
k1 = 2
sln = SubArraySumSolution(nums1, k1)

print(sln.solve())
