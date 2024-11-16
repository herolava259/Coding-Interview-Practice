from typing import List


class MaxProfitWithCooldownSolution:
    def __init__(self, prices: List[int]):
        self.prices: List[int] = prices

    def solve(self) -> int:
        n = len(self.prices)
        dp: List[int] = [0] * n
        max_dp = 0
        lower: List[int] = [i - 1 for i in range(n)]

        for i in range(1, n):
            lower_i = lower[i]
            if i == 5:
                pass
            while lower_i >= 0 and self.prices[lower_i] > self.prices[i]:
                lower_i = lower[lower_i]
            lower[i] = lower_i

            cur_dp = max_dp

            while lower_i >= 0:
                cd_dp = self.prices[i] - self.prices[lower_i]
                if lower_i - 2 >= 0:
                    cd_dp += dp[lower_i - 2]
                cur_dp = max(cur_dp, cd_dp)

                lower_i = lower[lower_i]

            dp[i] = max_dp = cur_dp

        return max_dp


prices1 = [1, 2, 3, 0, 2, 5, 4, 100]
sln = MaxProfitWithCooldownSolution(prices1)

print(sln.solve())
