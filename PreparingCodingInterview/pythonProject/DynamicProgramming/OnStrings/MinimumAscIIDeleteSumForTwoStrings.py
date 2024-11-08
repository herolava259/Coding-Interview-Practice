from typing import List


class MinimumDeleteSumSolution:
    def __init__(self, s1: str, s2: str):
        self.s1: str = s1
        self.s2: str = s2

    def solve(self) -> int:
        m, n = len(self.s1), len(self.s2)

        dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

        cost_s = total_cost(self.s1) + total_cost(self.s2)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0
                if self.s1[i - 1] == self.s2[j - 1]:
                    cost = dp[i - 1][j - 1] + ord(self.s1[i - 1])
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], cost)

        return cost_s - 2 * dp[m][n]


def total_cost(s: str):
    sums = 0
    for c in s:
        sums += ord(c)

    return sums


s1 = "kakakakaka"
s2 = "kekakaka"

sln = MinimumDeleteSumSolution(s1, s2)

print(sln.solve())
