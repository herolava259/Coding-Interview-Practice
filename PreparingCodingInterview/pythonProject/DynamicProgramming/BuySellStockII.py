from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = []
        n = len(prices)
        lower = [i-1 for i in range(n)]
        lower[0] = -1
        for i in range(1, n):
            p = lower[i]
            while p >= 0 and prices[p] > prices[i]:
                p = lower[p]
            lower[i] = p

        dp.append(0)
        max_dp = 0
        for i in range(1, n):
            if lower[i] == -1:
                dp.append(max_dp)
                continue

            max_dp = max(max_dp, prices[i] - prices[lower[i]] + dp[lower[i]])
            dp.append(max_dp)
        return max_dp


sln = Solution()

prices = [1,2,3,4,5]
print(sln.maxProfit(prices))
