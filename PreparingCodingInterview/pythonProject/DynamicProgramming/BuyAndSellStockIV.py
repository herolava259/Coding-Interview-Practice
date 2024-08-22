from typing import List


class MaxProfitIV:
    def __init__(self, k: int, prices: List[int]):
        self.k: int = k
        self.prices: List[int] = prices

    def solve(self) -> int:
        n = len(self.prices)
        single_dp: List[List[int]] = [[0] * n for _ in range(n)]

        for i in range(n):
            max_profit: int = 0
            min_price, max_price = self.prices[i], self.prices[i]
            for j in range(i + 1, n):
                cur_price = self.prices[j]

                if cur_price > max_price:
                    max_price = cur_price
                elif cur_price < min_price:
                    min_price = max_price = cur_price

                if max_price - min_price > max_profit:
                    max_profit = max_price - min_price

                single_dp[i][j] = max_profit
        k_dp = [[0] * (self.k + 1) for _ in range(n + 1)]

        for i in range(1, self.k + 1):
            for j in range(n):
                k_dp[j][i] = k_dp[j][i - 1]
                for p in range(j):
                    k_dp[j][i] = max(k_dp[p][i - 1] + single_dp[p][j], k_dp[p][i], k_dp[j][i])

        return k_dp[n - 1][self.k]

    def fast_solve(self) -> int:
        n = len(self.prices)
        lower_idx: List[int] = [-1] * n
        for i in range(1, n):
            cur_price = self.prices[i]
            idx = i-1
            while idx >= 0 and cur_price <= self.prices[idx]:
                idx = lower_idx[idx]
            lower_idx[i] = idx

        k_dp = [[0] * (self.k+1) for _ in range(n)]

        for i in range(1, self.k+1):
            for j in range(1, n):
                k_dp[j][i] = max(k_dp[j][i-1], k_dp[j-1][i])
                idx = lower_idx[j]
                while idx >= 0:
                    if k_dp[idx][i-1] + self.prices[j] - self.prices[idx] > k_dp[j][i]:
                        k_dp[j][i] = k_dp[idx][i-1] + self.prices[j] - self.prices[idx]
                    idx = lower_idx[idx]

        return k_dp[n-1][self.k]

    def faster_solve(self) -> int:
        curr_dp: List[List[int]] = [[0] * 2 for _ in range(self.k+1)]
        prev_dp: List[List[int]] = [[0] * 2 for _ in range(self.k+1)]

        for i in range(1, self.k+1):
            prev_dp[i][0] = -self.prices[0]

        max_res = 0
        for p in self.prices[1:]:

            for i in range(1, self.k+1):
                curr_dp[i][0] = max(prev_dp[i-1][1]-p, prev_dp[i][0])

            for i in range(1, self.k+1):
                curr_dp[i][1] = max(prev_dp[i][0] + p, prev_dp[i][1])
                max_res = max(max_res, curr_dp[i][1])

            prev_dp, curr_dp = curr_dp, prev_dp

        return max_res

k1, prices1 = 2, [5, 4, 3]

sln = MaxProfitIV(k1, prices1)

print(sln.faster_solve())
