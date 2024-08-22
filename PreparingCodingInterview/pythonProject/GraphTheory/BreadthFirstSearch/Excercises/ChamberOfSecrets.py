from typing import List
from collections import deque


class TargetEdge:
    def __init__(self, nid: int, c: 0 | 1):
        self.nid: int = nid
        self.c: 0 | 1 = c


class ChamberOfSecretsSolution:
    def __init__(self, m_row: int, n_col: int, matrix: List[List[str]]):
        self.m_row: int = m_row
        self.n_col: int = n_col
        self.mtx: List[List[str]] = matrix

    def simulate_problem(self) -> (List[List[TargetEdge]], List[List[int]]):

        nid_mtx = [[-1 for _ in range(self.n_col)] for _ in range(self.m_row)]
        counter = 0
        coords: List[tuple] = []
        for i in range(self.m_row):
            for j in range(self.n_col):
                if self.mtx == '#':
                    coords.append((i, j))
                    nid_mtx[i][j] = counter
                    counter += 1
        g: List[List[TargetEdge]] = [[] for _ in range(2 * counter)]
        for idx, coord in enumerate(coords):

            src_i, src_j = 2 * idx, 2 * idx + 1
            counter += 2
            c_i, c_j = coord

            for i in range(c_i, -1, -1):
                if self.mtx[i][c_j] == '#':
                    dst_nid = nid_mtx[i][c_j]
                    dst_i, dst_j = dst_nid * 2, dst_nid * 2 + 1
                    g[src_i].extend([TargetEdge(dst_i, 0), TargetEdge(dst_j, 1)])
                    g[src_j].extend([TargetEdge(dst_i, 1), TargetEdge(dst_j, 0)])
                    break
            for i in range(c_i + 1, self.m_row):
                if self.mtx[i][c_j] == '#':
                    dst_nid = nid_mtx[i][c_j]
                    dst_i, dst_j = dst_nid * 2, dst_nid * 2 + 1
                    g[src_i].extend([TargetEdge(dst_i, 0), TargetEdge(dst_j, 1)])
                    g[src_j].extend([TargetEdge(dst_i, 1), TargetEdge(dst_j, 0)])
                    break
            for j in range(c_j, -1, -1):
                if self.mtx[c_i][j] == '#':
                    dst_nid = nid_mtx[c_i][j]
                    dst_i, dst_j = dst_nid * 2, dst_nid * 2 + 1
                    g[src_i].extend([TargetEdge(dst_i, 0), TargetEdge(dst_j, 1)])
                    g[src_j].extend([TargetEdge(dst_i, 1), TargetEdge(dst_j, 0)])
                    break
            for j in range(c_j + 1, self.n_col):
                if self.mtx[c_i][j] == '#':
                    dst_nid = nid_mtx[c_i][j]
                    dst_i, dst_j = dst_nid * 2, dst_nid * 2 + 1
                    g[src_i].extend([TargetEdge(dst_i, 0), TargetEdge(dst_j, 1)])
                    g[src_j].extend([TargetEdge(dst_i, 1), TargetEdge(dst_j, 0)])
                    break

        en_nid_j = len(g)
        if coords[0][0] > 0:
            return g, -1, -1, -1

        adj_en_id = nid_mtx[coords[0][0]][coords[0][1]]
        nid_i, nid_j = adj_en_id * 2, adj_en_id * 2 + 1
        g.append([TargetEdge(nid_i, 1), TargetEdge(nid_j, 0)])
        g[nid_j].append(TargetEdge(en_nid_j, 0))
        g[nid_i].append(TargetEdge(en_nid_j, 1))

        if coords[-1][0] < self.m_row - 1:
            return g, -1, -1, -1

        st_id = nid_mtx[coords[-1][0]][coords[-1][1]]
        st_nid_i, st_nid_j = st_id * 2, st_id * 2 + 1

        return g, en_nid_j, st_nid_i, st_nid_j

    def bfs_solve(self) -> int:

        g, en_nid_j, st_nid_i, st_nid_j = self.simulate_problem()

        if en_nid_j == -1:
            return -1
        n = len(g)
        d_cost = [100_000_001 for _ in range(n)]

        d_cost[st_nid_i] = 1
        d_cost[st_nid_j] = 0
        dq: deque = deque()
        dq.appendleft(st_nid_j)
        dq.append(st_nid_i)

        while dq:
            curr_u = dq.popleft()

            if curr_u == en_nid_j:
                return d_cost[en_nid_j]
            for e in g[curr_u]:
                if d_cost[curr_u] + e.c >= d_cost[e.nid]:
                    continue
                d_cost[e.nid] = d_cost[curr_u] + e.c
                if e.c == 1:
                    dq.append(e.nid)
                else:
                    dq.appendleft(e.nid)

        return -1
