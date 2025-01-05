from typing import List
import math


class PerfectSquaresSolution:
    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:
        sqrt_n = int(math.sqrt(self.n))
        dp: List[int] = [100000000] * (self.n + 1)

        dp[0] = 0
        for i in range(1, sqrt_n + 1):
            dp[i ** 2] = 1

        for i in range(1, self.n + 1):
            if dp[i] == 1:
                continue
            for j in range(1, sqrt_n + 1):
                if j ** 2 >= i:
                    break
                dp[i] = min(1 + dp[i - j ** 2], dp[i])

        return dp[self.n]


n = 13

sln = PerfectSquaresSolution(n)

print(sln.solve())
