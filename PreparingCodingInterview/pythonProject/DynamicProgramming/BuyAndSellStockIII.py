from typing import List


class MaxProfitIII:
    def __init__(self, prices: List[int]):
        self.prices: List[int] = prices

    def solve(self) -> int:
        n = len(self.prices)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            min_e, max_e = self.prices[i], self.prices[i]
            max_profit = 0
            for j in range(i + 1, n):

                cur_price = self.prices[j]

                if cur_price > max_e:
                    max_e = cur_price
                elif cur_price < min_e:
                    min_e = cur_price
                    max_e = min_e
                max_profit = max(max_profit, max_e-min_e)
                dp[i][j] = max_profit

        max_res = dp[0][n - 1]

        for i in range(1, n):
            tmp_max = dp[0][i - 1] + dp[i][n - 1]

            max_res = max(tmp_max, max_res)

        return max_res

    def fast_solve(self) -> int:
        last_dp: List[int] = []
        n = len(self.prices)

        min_price, max_price = self.prices[-1], self.prices[-1]
        max_profit = 0
        last_dp.append(max_profit)

        for i in range(n - 2, -1, -1):
            cur_price = self.prices[i]

            if cur_price > max_price:
                min_price = max_price = cur_price
            elif cur_price < min_price:
                min_price = cur_price
            if max_profit < max_price - min_price:
                max_profit = max_price - min_price
            last_dp.insert(0, max_profit)

        max_two_profit = 0

        min_price, max_price = self.prices[0], self.prices[0]
        max_profit = max_price - min_price

        for i in range(1, n):
            max_two_profit = max(max_two_profit, max_profit + last_dp[i])
            cur_price = self.prices[i]
            if cur_price > max_price:
                max_price = cur_price
            elif cur_price < min_price:
                max_price = min_price = cur_price

            if max_profit < max_price - min_price:
                max_profit = max_price - min_price

        return max(max_two_profit, max_profit)


prices1 = [2,1,4,5,2,9,7]

sln = MaxProfitIII(prices1)

print(sln.fast_solve())
