from typing import List, Deque, Tuple
from collections import deque


class RottingOrangesSolution:
    def __init__(self, grid: List[List[int]]):

        self.grid: List[List[int]] = grid

    def solve(self) -> int:

        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q: Deque[Tuple[int, int, int]] = deque()

        num_fresh_orange = 0

        m_row, n_col = len(self.grid), len(self.grid[0])

        for i in range(m_row):
            for j in range(n_col):
                if self.grid[i][j] == 2:
                    q.append((i, j, 0))
                elif self.grid[i][j] == 1:
                    num_fresh_orange += 1

        cur_time = 0
        while q:
            cur_i, cur_j, cur_time = q.popleft()

            for dir_i, dir_j in directions:
                nxt_i, nxt_j = cur_i + dir_i, cur_j + dir_j

                if not (0 <= nxt_i < m_row) or not (0 <= nxt_j < n_col):
                    continue
                if self.grid[nxt_i][nxt_j] != 1:
                    continue
                self.grid[nxt_i][nxt_j] = 2
                num_fresh_orange -= 1
                q.append((nxt_i, nxt_j, cur_time + 1))

        if num_fresh_orange > 0:
            return -1
        return cur_time


grid1 = [[0,2]]

sln = RottingOrangesSolution(grid1)

print(sln.solve())
