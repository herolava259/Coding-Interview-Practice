from typing import List
from collections import deque

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class KathiresanEscapeSolution:
    def __init__(self, m_row: int, n_col: int, matrix: List[List[str]]):

        self.m_row = m_row
        self.n_col = n_col
        self.mtx = matrix

    def bfs_solve(self) -> int:

        dq: deque = deque()

        cur_x, cur_y = 0, 0
        end_x, end_y = self.m_row - 1, self.n_col - 1

        num_kills = [[100_000_008 for _ in range(self.n_col)] for _ in range(self.m_row)]
        num_kills[0][0] = 0
        dq.append((cur_x, cur_y))

        while dq:

            cur_x, cur_y = dq.popleft()

            if cur_y == end_x and cur_y == end_y:
                return num_kills[cur_x][cur_y]
            for offset in offsets:
                new_x, new_y = cur_x + offset[0], cur_y + offset[1]
                if not (0 <= new_x < self.m_row and 0 <= new_y < self.n_col):
                    continue
                cost = 1
                if self.mtx[new_x][new_y] == self.mtx[cur_x][cur_y]:
                    cost = 0
                if cost + num_kills[cur_x][cur_y] >= num_kills[new_x][new_y]:
                    continue
                num_kills[new_x][new_y] = cost + num_kills[cur_x][cur_y]
                if cost == 1:
                    dq.append((new_x, new_y))
                else:
                    dq.appendleft((new_x, new_y))

        return num_kills[end_x][end_y]
