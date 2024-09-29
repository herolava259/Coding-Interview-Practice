from typing import List, Deque as Queue, Tuple as Pair
from collections import deque as queue


class ZeroOneMatrixSolution:
    def __init__(self, mat: List[List[int]]):
        self.mtx: List[List[int]] = mat
        self.m_row: int = len(mat)
        self.n_col: int = len(mat[0])
        self.directions: List[Pair[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve(self):
        # init result matrix
        count_mtx: List[List[int]] = [[100000] * self.n_col for _ in range(self.m_row)]

        for i in range(self.m_row):
            for j in range(self.n_col):
                if self.mtx[i][j] == 0:
                    count_mtx[i][j] = 0
                    self.bfs_nearest(i, j, count_mtx)

        return count_mtx

    def bfs_nearest(self, beg_i: int, beg_j: int, count_mtx: List[List[int]]):

        q: Queue[Pair[int, int]] = queue()

        q.append((beg_i, beg_j))
        self.mtx[beg_i][beg_j] = 2

        while q:
            cur_i, cur_j = q.popleft()

            for offset_i, offset_j in self.directions:
                near_i, near_j = cur_i + offset_i, cur_j + offset_j
                if not (0 <= near_i < self.m_row and 0 <= near_j < self.n_col):
                    continue
                if self.mtx[near_i][near_j] == 0:
                    self.mtx[near_i][near_j] = 2
                    count_mtx[near_i][near_j] = 0
                    q.appendleft((near_i, near_j))
                elif self.mtx[near_i][near_j] == 1 and count_mtx[cur_i][cur_j] + 1 < count_mtx[near_i][near_j]:
                    count_mtx[near_i][near_j] = count_mtx[cur_i][cur_j] + 1
                    q.append((near_i, near_j))


mat1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

sln = ZeroOneMatrixSolution(mat1)

print(sln.solve())
