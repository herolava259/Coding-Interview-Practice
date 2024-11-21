from typing import List

class CoinChangeIISolution:
    def __init__(self, amount: int, coins: List[int]):
        self.amount: int = amount
        self.coins: List[int] = coins
    def solve(self) -> int:
        len_coins = len(self.coins)
        dp: List[List[int]] = [[0] * len_coins for _ in range(self.amount+1)]
        for i in range(len_coins):
            dp[0][i] = 1

        coins: List[int] = sorted(self.coins)
        for am in range(1, self.amount+1):

            if am < coins[0]:
                continue
            dp[am][0] = dp[am-coins[0]][0]
            for i in range(1,len_coins):
                dp[am][i] = dp[am][i - 1]
                if am >= coins[i]:
                    dp[am][i] += dp[am-coins[i]][i]
        return dp[self.amount][-1]

amount1 = 10
coins1: List[int] = [10]

sln = CoinChangeIISolution(amount1, coins1)

print(sln.solve())

