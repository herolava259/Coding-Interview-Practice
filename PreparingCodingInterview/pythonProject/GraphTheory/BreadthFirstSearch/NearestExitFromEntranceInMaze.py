from typing import List, Deque, Tuple
from collections import deque


class NearestExitSolution:

    def __init__(self, maze: List[List[str]], entrance: List[int]):
        self.maze: List[List[str]] = maze
        self.entrance: List[int] = entrance

    def solve(self) -> int:
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m_row, n_col = len(self.maze), len(self.maze[0])
        q: Deque[Tuple[int, int, int]] = deque()

        cur_i, cur_j = self.entrance
        cur_num_step: int = 0
        self.maze[cur_i][cur_j] = '+'

        for dir in directions:
            nxt_i, nxt_j = cur_i + dir[0], cur_j + dir[1]

            if not (0 <= nxt_i < m_row) or not (0 <= nxt_j < n_col) or self.maze[nxt_i][nxt_j] == "+":
                continue
            nxt_num_step = cur_num_step + 1
            self.maze[nxt_i][nxt_j] = "+"
            q.append((nxt_i, nxt_j, nxt_num_step))

        while q:
            cur_i, cur_j, cur_num_step = q.popleft()

            if cur_i == 0 or cur_i == m_row-1 or cur_j == 0 or cur_j == n_col-1:
                return cur_num_step

            for dir in directions:
                nxt_i, nxt_j = cur_i + dir[0], cur_j + dir[1]

                if self.maze[nxt_i][nxt_j] == "+":
                    continue
                nxt_num_step = cur_num_step + 1
                self.maze[nxt_i][nxt_j] = "+"
                q.append((nxt_i, nxt_j, nxt_num_step))
        return -1


maze1 = [[".","+"]]
entrance1 = [0,0]

sln = NearestExitSolution(maze1, entrance1)

print(sln.solve())
