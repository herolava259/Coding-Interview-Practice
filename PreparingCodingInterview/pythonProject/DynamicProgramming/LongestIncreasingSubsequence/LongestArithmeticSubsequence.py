from typing import List


class LongestArithmeticSubsequenceSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:
        max_val = max(self.nums)
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        max_dp = 0
        for c in self.nums:
            for prev in range(max_val + 1):
                if prev == c:
                    dp[c][c] += 1
                    continue
                step = c - prev
                before = prev - step
                if dp[prev][prev] != 0:
                    dp[c][prev] = max(2, dp[c][prev])

                if before < 0 or before > max_val:
                    continue
                dp[c][prev] = max(dp[prev][before] + 1, dp[c][prev])
                max_dp = max(max_dp, dp[c][prev])

        return max_dp


nums1 = [0,500]

sln = LongestArithmeticSubsequenceSolution(nums1)
print(sln.solve())
