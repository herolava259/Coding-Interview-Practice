from typing import List
from collections import deque

directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
inf = 10 ** 9 + 7


class MinimumCostPathSolution:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.m_row = len(grid)
        self.n_col = len(grid[0])

    def bfs_solve(self):

        d_cost = [[inf for _ in range(self.n_col)] for _ in range(self.m_row)]

        d_cost[0][0] = 0

        dq: deque = deque()
        curr_i, curr_j = 0, 0
        en_i, en_j = self.m_row - 1, self.n_col - 1
        dq.appendleft((curr_i, curr_j))

        while dq:
            curr_i, curr_j = dq.popleft()
            if curr_i == en_i and curr_j == en_j:
                break

            curr_dir = self.grid[curr_i][curr_j]

            for dir in directions.keys():
                cost = 1
                offset_x, offset_y = directions[dir]
                next_i, next_j = curr_i + offset_x, curr_j + offset_y

                if not (0 <= next_i < self.m_row and 0 <= next_j < self.n_col):
                    continue
                if dir == curr_dir:
                    cost = 0
                if cost + d_cost[curr_i][curr_j] >= d_cost[next_i][next_j]:
                    continue
                d_cost[next_i][next_j] = cost + d_cost[curr_i][curr_j]
                if cost == 1:
                    dq.append((next_i, next_j))
                else:
                    dq.appendleft((next_i, next_j))

        return d_cost[en_i][en_j]

grid = [[1,2],[4,3]]

sln = MinimumCostPathSolution(grid)

print(sln.bfs_solve())

