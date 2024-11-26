from typing import List


class NumDistinctSolution:
    def __init__(self, s: str, t: str):

        self.source: str = s
        self.target: str = t

    def solve(self) -> int:

        n_s, n_t = len(self.source), len(self.target)

        dp: List[List[int]] = [[0] * (n_t+1) for _ in range(n_s + 1)]

        for i in range(n_s+1):
            dp[i][0] = 1

        for i in range(1, n_s+1):
            for j in range(1, n_t+1):
                total_distinct = 0

                if self.source[i-1] == self.target[j-1]:
                    total_distinct += dp[i-1][j-1]

                total_distinct += dp[i-1][j]

                dp[i][j] = total_distinct

        return dp[n_s][n_t]

s1 = 'rabbbit'
t1 = 'rabbit'

sln = NumDistinctSolution(s1, t1)

print(sln.solve())

