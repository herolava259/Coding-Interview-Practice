from typing import List

class CountNegativesSolution:
    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid

    def solve(self) -> int:

        m_row, n_col = len(self.grid), len(self.grid[0])

        num_neg = 0

        for i in range(m_row):

            low, high = 0, n_col-1

            while low < high:

                mid = (low+high) // 2

                val = self.grid[i][mid]

                if val >= 0:
                    low = mid+1
                else:
                    high = mid

            if self.grid[i][low] < 0:
                num_neg += n_col - low

        return num_neg


grid =[[3,2],[1,0]]
sln = CountNegativesSolution(grid)

print(sln.solve())
