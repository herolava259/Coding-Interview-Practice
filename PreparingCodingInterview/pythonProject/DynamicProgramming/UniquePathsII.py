from typing import List


class UniquePathsIISolution:
    def __init__(self, obstacle_grid: List[List[int]]):
        self.grid: List[List[int]] = obstacle_grid
        self.m: int = len(self.grid)
        self.n: int = len(self.grid[0])

    def solve(self) -> int:
        prev_dp = [0 for _ in range(self.n)]

        for i in range(self.n):
            if self.grid[0][i] == 1:
                break
            prev_dp[i] = 1

        for i in range(1, self.m):
            cur_dp = []
            for j in range(self.n):
                if self.grid[i][j]:
                    cur_dp.append(0)
                    continue
                num_path = prev_dp[j]
                if j > 0:
                    num_path += cur_dp[-1]
                cur_dp.append(num_path)
            prev_dp = cur_dp

        return prev_dp[-1]


obstacleGrid1 = [[0,1],[0,0]]

sln = UniquePathsIISolution(obstacleGrid1)

print(sln.solve())
