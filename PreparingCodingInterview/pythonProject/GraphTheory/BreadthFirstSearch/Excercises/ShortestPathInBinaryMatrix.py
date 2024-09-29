from typing import List, Deque as Queue, Tuple
from collections import deque as queue


class ShortestPathSolution:
    def __init__(self, grid: List[List[int]]):

        self.grid: List[List[int]] = grid

    def solve(self) -> int:

        n = len(self.grid)
        if self.grid[0][0] == 1:
            return -1

        q: Queue[Tuple[int, int, int]] = queue()

        q.append((0, 0, 1))
        self.grid[0][0] = 2

        while q:
            cur_i, cur_j, len_path = q.popleft()

            if cur_i == n - 1 and cur_j == n - 1:
                return len_path

            for move_row in (-1, 0, 1):
                near_i = cur_i + move_row

                if not (0 <= near_i < n):
                    continue

                for move_col in (-1, 0, 1):
                    if move_row == 0 and move_col == 0:
                        continue
                    near_j = cur_j + move_col

                    if not (0 <= near_j < n):
                        continue
                    if self.grid[near_i][near_j] != 0:
                        continue

                    self.grid[near_i][near_j] = 2

                    q.append((near_i, near_j, len_path + 1))

        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]

sln = ShortestPathSolution(grid)

print(sln.solve())