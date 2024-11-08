from typing import List
from collections import Counter


class DeleteAndEarnSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:
        nums_freq: Counter = Counter(self.nums)

        dp = [0] * 10001
        max_dp = [0] * 10001

        dp[0] = 0
        dp[1] = nums_freq[1]

        max_dp[1] = dp[1]

        for weight in range(2, 10001):
            dp[weight] += weight * nums_freq[weight] + max_dp[weight - 2]
            max_dp[weight] = max(max_dp[weight-1], dp[weight])
        return max_dp[-1]


nums = [8,10,4,9,1,3,5,9,4,10]
sln = DeleteAndEarnSolution(nums)

print(sln.solve())
