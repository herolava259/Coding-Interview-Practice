from typing import List
from queue import Queue


class VmunchSolution:
    def __init__(self, matrix: List[List[str]], b_pos: tuple, c_pos: tuple):

        self.m_row: int = len(matrix)
        self.n_col: int = len(matrix[0])
        self.board: List[List[str]] = matrix
        self.s_i: int = b_pos[0]
        self.s_j: int = b_pos[1]
        self.e_i: int = c_pos[0]
        self.e_j: int = c_pos[1]

        self.visited: List[List[bool]] = [[False for _ in range(self.n_col)] for _ in range(self.m_row)]
        self.prev: List[List[int]] = [[-1 for _ in range(self.n_col)] for _ in range(self.m_row)]

    def bfs_solve(self) -> (int, List[tuple]):

        move_x = [0, 0, 1, -1]
        move_y = [1, -1, 0, 0]

        d_min = 2_000_000_007
        path: List[tuple] = []
        q: Queue = Queue(maxsize=self.m_row * self.n_col)

        q.put((self.s_i, self.s_j))
        self.visited[self.s_i][self.s_j] = True
        pos_i, pos_j = self.s_i, self.s_j
        while not q.empty():
            pos_i, pos_j = q.get()

            if self.board[pos_i][pos_j] == 'B':
                break
            for offset_i, offset_j in zip(move_x, move_y):
                nxt_i, nxt_j = pos_i + offset_i, pos_j + offset_j

                if nxt_i < 0 or nxt_i >= self.m_row or nxt_j < 0 or nxt_j >= self.n_col:
                    continue
                if self.visited[nxt_i][nxt_j] or self.board[nxt_i][nxt_j] == "*":
                    continue
                q.put((nxt_i, nxt_j))
                self.visited[nxt_i][nxt_j] = True
                self.prev[nxt_i][nxt_j] = pos_i * self.n_col + pos_j

        while self.board[pos_i][pos_j] != "C":
            path.insert(0, (pos_i, pos_j))
            d_min += 1
            nid = self.prev[pos_i][pos_j]
            pos_i = nid // self.n_col
            pos_j = nid % self.n_col

        path.insert(0, (pos_i, pos_j))

        return d_min, path







