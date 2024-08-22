from typing import List
from collections import deque

directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]


class CycleInMazeSolution:
    def __init__(self, m_row: int, n_col: int, k: int, matrix: List[List[str]]):
        self.m_row = m_row
        self.n_col = n_col
        self.k = k
        self.mtx: List[List[str]] = matrix

    def find_init_position(self) -> tuple:

        for i in range(self.m_row):
            for j in range(self.n_col):
                if self.mtx[i][j] == 'X':
                    return i, j
        return 0, 0

    def bfs_solve(self) -> str:

        beg_i, beg_j = self.find_init_position()

        cur_i, cur_j, c = beg_i, beg_j, 0
        path = ''

        q: deque = deque()

        q.append((cur_i, cur_j, c, path))
        while q:
            cur_i, cur_j, c, path = q.popleft()

            if c >= self.k and (cur_i != beg_i or cur_j != beg_j):
                continue

            if c == self.k and cur_i == beg_i and cur_j == beg_j:
                break

            for dir in directions:
                new_i, new_j = cur_i + dir[0], cur_j + dir[1]

                if not (0 <= new_i < self.m_row and 0 <= new_j < self.n_col):
                    continue
                if self.mtx[new_i][new_j] == '*':
                    continue
                new_path = path + get_sign((cur_i, cur_j), (new_i, new_j))
                q.append((new_i, new_j, c + 1, new_path))

        if cur_i != beg_i or cur_j != beg_j:
            return 'IMPOSSIBLE'

        return path


def get_sign(pos_1: tuple, pos_2):
    i1, j1 = pos_1
    i2, j2 = pos_2

    if i1 == i2 and j1 < j2:
        return 'R'
    elif i1 == i2 and j1 > j2:
        return 'L'
    elif j1 == j2 and i1 < i2:
        return 'D'
    elif j1 == j2 and i1 > i2:
        return 'U'
    return '$'


n1, m1, k1 = 5, 6, 14

raw_b = '''..***.
*...X.
..*...
..*.**
....*.'''

raw_b = raw_b.split('\n')

mtx1 = [list(l) for l in raw_b]

sln1 = CycleInMazeSolution(n1, m1, k1, mtx1)

print(sln1.bfs_solve())

result = 'DLDDLLLRRRUURU'
