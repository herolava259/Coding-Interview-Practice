from typing import List


class MinimumFallingPathSumSolution:
    def __init__(self, matrix: List[List[int]]):
        self.matrix: List[List[int]] = matrix

    def solve(self) -> int:

        m_row = len(self.matrix)
        n_col = len(self.matrix[0])

        dp = list(self.matrix[0])
        tmp_dp = [0] * n_col

        for i in range(1, m_row):
            for j in range(1, n_col - 1):
                tmp_dp[j] = min(dp[j - 1], dp[j], dp[j + 1]) + self.matrix[i][j]

            tmp_dp[0] = min(dp[0], dp[1]) + self.matrix[i][0]
            tmp_dp[-1] = min(dp[-1], dp[-2]) + self.matrix[i][-1]

            tmp_dp, dp = dp, tmp_dp

        return min(dp)


mtx1 = [[-19,57],[-40,-5]]
sln = MinimumFallingPathSumSolution(mtx1)

print(sln.solve())
