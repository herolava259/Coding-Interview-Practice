from typing import List

class CombinationSumIVSolution:
    def __init__(self, nums: List[int], target: int):
        self.nums: List[int] = nums
        self.target: int = target

    def solve(self) -> int:

        dp = [0] * (self.target+1)

        coins: List[int] = sorted(self.nums)

        dp[0] = 1

        for am in range(1, self.target+1):

            for c in coins:
                if am < c:
                    continue
                dp[am] += dp[am-c]

        return dp[self.target]

nums1 = [1, 2, 3]
target1 = 4

sln = CombinationSumIVSolution(nums1, target1)

print(sln.solve())