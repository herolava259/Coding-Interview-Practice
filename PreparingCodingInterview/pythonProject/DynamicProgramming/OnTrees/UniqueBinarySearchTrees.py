from typing import List


class NumTreesSolution:
    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:

        dp: List[int] = [0] * (self.n + 1)

        dp[1] = 1
        dp[0] = 1

        for i in range(2, self.n + 1):
            for j in range(i):
                dp[i] += dp[i - 1 - j] * dp[j]

        return dp[self.n]


n1 = 3

sln = NumTreesSolution(n1)
print(sln.solve())
