from typing import List
from collections import deque


class TargetEdge:
    def __init__(self, v: int, c: 0 | 1):
        self.v: int = v
        self.c: 0 | 1 = c


class OkabeAndCitySolution:
    def __init__(self, m_row: int, n_col: int, ligt_pos: List[tuple]):

        self.m_row = m_row
        self.n_col = n_col

        self.light_pos: List[tuple] = ligt_pos

    def simulate_problem(self) -> (List[TargetEdge], int, int):

        k = len(self.light_pos)
        mtx = [[-1 for _ in range(self.n_col)] for _ in range(self.m_row)]

        for idx, l in enumerate(self.light_pos):
            l_i, l_j = l[0] - 1, l[1] - 1

            mtx[l_i][l_j] = idx
        g: List[List[TargetEdge]] = [[] for _ in range(k)]

        for idx, l in enumerate(self.light_pos):
            l_i, l_j = l[0] - 1, l[1] - 1

            for i in range(self.m_row):
                if i == l_i or mtx[i][l_j] == -1:
                    continue
                if abs_diff(i, l_i) <= 1:
                    g[idx].append(TargetEdge(mtx[i][l_j], 0))
                else:
                    g[idx].append(TargetEdge(mtx[i][l_j], 1))

            for j in range(self.n_col):
                if j == l_i or mtx[l_i][j] == -1:
                    continue
                if abs_diff(j, l_j) <= 1:
                    g[idx].append(TargetEdge(mtx[l_i][j], 0))
                else:
                    g[idx].append(TargetEdge(mtx[l_i][j], 1))

        return g, 0, k - 1

    def bfs_solve(self) -> int:

        dq: deque = deque()

        g, beg, end = self.simulate_problem()
        k = len(g)
        d_cost = [100_000_009 for _ in range(k)]

        d_cost[beg] = 0
        cur = beg
        dq.append(cur)

        while dq:
            cur = dq.popleft()

            if cur == end:
                return d_cost[end]

            for e in g[cur]:

                if e.c + d_cost[cur] >= d_cost[e.v]:
                    continue
                d_cost[e.v] = e.c + d_cost[cur]

                if e.c == 1:
                    dq.append(e.v)
                else:
                    dq.appendleft(e.v)

        return -1


def abs_diff(a: int, b: int):
    return a - b if a >= b else b - a
