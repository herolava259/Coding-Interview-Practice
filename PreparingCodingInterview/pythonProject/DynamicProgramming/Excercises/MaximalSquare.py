from typing import List


class MaximalSquareSolution:

    def __init__(self, matrix: List[List[str]]):

        self.mtx: List[List[str]] = matrix

    def solve(self) -> int:
        m, n = len(self.mtx), len(self.mtx[0])
        prev_dp: List[int] = [0 for _ in range(n)]
        curr_dp: List[int] = [0 for _ in range(n)]
        max_len = 0

        for i in range(m):
            for j in range(n):
                cur_pixel = self.mtx[i][j]
                if i == 0 or j == 0:
                    curr_dp[j] = 1 if cur_pixel == '1' else 0
                    max_len = max(curr_dp[j], max_len)
                    continue
                if cur_pixel == '0':
                    curr_dp[j] = 0
                    continue
                curr_dp[j] = 1
                above_pixel = self.mtx[i - 1][j]
                left_pixel = self.mtx[i][j - 1]
                diag_pixel = self.mtx[i-1][j-1]
                if above_pixel == '0' or left_pixel == '0' or diag_pixel == '0':
                    max_len = max(curr_dp[j], max_len)
                    continue

                curr_dp[j] = min(prev_dp[j], curr_dp[j - 1]) + 1

                if self.mtx[i-curr_dp[j]+1][j-curr_dp[j]+1] == '0':
                    curr_dp[j] -= 1
                max_len = max(max_len, curr_dp[j])

            curr_dp, prev_dp = prev_dp, curr_dp

        return max_len * max_len


matrix1 = [["0"]]

sln = MaximalSquareSolution(matrix1)

print(sln.solve())
