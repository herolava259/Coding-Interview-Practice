from typing import List


class MaxProfitSolution:

    def __init__(self, prices: List[int], fee: int):
        self.prices: List[int] = prices
        self.fee: int = fee

    def solve(self) -> int:
        max_profits_end_buy: List[int] = [0] * (len(self.prices))

        max_profits_end_sell: List[int] = [0] * (len(self.prices))

        max_profits_end_buy[0] = -self.prices[0]

        for i in range(1, len(self.prices)):

            max_profits_end_buy[i] = max(max_profits_end_buy[i - 1],
                                         max_profits_end_sell[i - 1] - self.prices[i])

            max_profits_end_sell[i] = max(max_profits_end_sell[i - 1],
                                          max_profits_end_buy[i - 1] + self.prices[i] - self.fee)

        return max_profits_end_sell[-1]


prices1 = [1,3,7,5,10,3]
fee1 = 3

sln = MaxProfitSolution(prices1, fee1)

print(sln.solve())
