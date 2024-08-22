from typing import List
from queue import Queue

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class BCIslandSolution:
    def __init__(self, matrix: List[List[int]]):
        self.mtx = matrix
        self.m_row: int = len(matrix)
        self.n_col: int = len(matrix[0])

    def rise_level_solve(self, h: int) -> int:

        count_island = 0

        visited: List[List[bool]] = [[False for _ in range(self.n_col)] for _ in range(self.m_row)]

        for i in range(self.m_row):
            for j in range(self.n_col):
                if not visited[i][j]:
                    self.bfs_solve(h, (i, j), visited)
                    count_island += 1
        return count_island

    def bfs_solve(self, h: int, beg_pos: tuple, visited: List[List[bool]]):

        q: Queue = Queue()

        q.put(beg_pos)

        pos_i, pos_j = beg_pos
        visited[pos_i][pos_j] = True

        while not q.empty():

            pos_i, pos_j = q.get()

            for move in moves:
                new_pos_i, new_pos_j = pos_i + move[0], pos_j + move[1]

                if new_pos_i < 0 or new_pos_i >= self.m_row or new_pos_j < 0 or new_pos_j >= self.n_col:
                    continue

                if visited[new_pos_i][new_pos_j] or self.mtx[new_pos_i][new_pos_j] <= h:
                    continue

                visited[new_pos_i][new_pos_j] = True
                q.put((new_pos_j, new_pos_j))

    def solve(self) -> bool:

        max_h = -1

        for i in range(self.m_row):
            for j in range(self.n_col):
                if self.mtx[i][j] > max_h:
                    max_h = self.mtx[i][j]

        for h in range(max_h):
            count_island = self.rise_level_solve(h)

            if count_island > 1:
                return False

        return True
