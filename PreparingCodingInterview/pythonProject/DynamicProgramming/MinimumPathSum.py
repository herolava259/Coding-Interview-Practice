from typing import List


class MinimumPathSumSolution:

    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid

    def solve(self) -> int:
        m, n = len(self.grid), len(self.grid[0])
        cur_dp: List[int] = []
        sums = 0
        for i in range(n):
            sums += self.grid[0][i]
            cur_dp.append(sums)
        prev_dp: List[int] = cur_dp

        for i in range(1, m):
            cur_dp = []
            for j in range(n):
                min_path = prev_dp[j]
                if j > 0:
                    min_path = min(min_path, cur_dp[-1])

                cur_dp.append(min_path + self.grid[i][j])
            prev_dp = cur_dp

        return prev_dp[-1]


grid1 = [[1,2,3],[4,5,6]]

sln = MinimumPathSumSolution(grid1)

print(sln.solve())
