from typing import List, Tuple, Deque
from collections import deque


class ShortestBridgeSolution:

    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid
        self.n: int = len(self.grid)
        self.directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def find_one_pixel_position(self) -> Tuple[int, int]:
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    return i, j

        return -1, -1

    def mark_position_for_second_island(self) -> List[Tuple[int, int]]:

        q: Deque[Tuple[int, int]] = deque()

        pos_i, pos_j = self.find_one_pixel_position()

        q.append((pos_i, pos_j))

        self.grid[pos_i][pos_j] = 2

        bounding: List[Tuple[int, int]] = []

        while q:
            pos_i, pos_j = q.popleft()

            near_zero: bool = False

            for offset_i, offset_j in self.directions:
                nxt_i, nxt_j = pos_i + offset_i, pos_j + offset_j

                if not (0 <= nxt_i < self.n and 0 <= nxt_j < self.n):
                    continue

                if self.grid[nxt_i][nxt_j] == 0:
                    near_zero = True
                    continue
                elif self.grid[nxt_i][nxt_j] == 1:
                    self.grid[nxt_i][nxt_j] = 2
                    q.append((nxt_i, nxt_j))

            if near_zero:
                bounding.append((pos_i, pos_j))

        return bounding

    def solve(self) -> int:

        bounding = self.mark_position_for_second_island()
        q: Deque[Tuple[int, int, int]] = deque()
        for cur_i, cur_j in bounding:
            q.append((cur_i, cur_j, 0))

        while q:
            cur_i, cur_j, num_zero = q.popleft()

            for offset_i, offset_j in self.directions:
                nxt_i, nxt_j = cur_i + offset_i, cur_j + offset_j

                if not (0 <= nxt_i < self.n and 0 <= nxt_j < self.n):
                    continue
                if self.grid[nxt_i][nxt_j] == 2:
                    continue
                elif self.grid[nxt_i][nxt_j] == 1:
                    return num_zero
                elif self.grid[nxt_i][nxt_j] == 0:
                    self.grid[nxt_i][nxt_j] = 2
                    q.append((nxt_i, nxt_j, num_zero + 1))

        return -1


grid1 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

sln = ShortestBridgeSolution(grid1)

print(sln.solve())
