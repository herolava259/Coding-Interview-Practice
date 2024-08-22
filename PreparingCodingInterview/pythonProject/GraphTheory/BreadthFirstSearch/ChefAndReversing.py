from typing import List
from collections import deque, defaultdict
inf = 10 ** 9

class TargetEdge:
    def __init__(self, v: int, w: int = 0):
        self.v: int = v
        self.w: int = w


class ChefAndReversingSolution:
    def __init__(self, n: int, m: int, g: List[List[int]]):

        self.g: List[List[int]] = g
        self.m: int = m
        self.n: int = n

    def build_weighted_graph(self) -> List[defaultdict]:

        w_g = [defaultdict() for _ in range(self.n+1)]

        for u in range(1, self.n+1):
            for v in self.g[u]:
                w_g[u][v] = TargetEdge(u, 0)
                w_g[v][u] = TargetEdge(u, 1)

        return w_g

    def bfs_solve(self) -> (int, List[tuple]):

        prev: List[int] = [0 for _ in range(self.n+1)]

        d_min: List[int] = [inf for _ in range(self.n+1)]

        dq: deque = deque()

        w_g: List[defaultdict] = self.build_weighted_graph()
        dq.append(1)
        while dq:
            curr_u, w = dq.popleft()

            if curr_u == self.n:
                break

            for edge in w_g[curr_u]:

                if d_min[edge.v] > d_min[curr_u] + edge.w:
                    prev[edge.v] = curr_u

                    if edge.w == 1:
                        dq.append(edge.v)
                    else:
                        dq.appendleft(edge.v)

        changes: List[tuple] = []

        curr_u = self.n
        while curr_u != 1:
            prev_u = prev[curr_u]
            if w_g[prev_u][curr_u].w == 1:
                changes.append((curr_u, prev_u))

            curr_u = prev_u

        return d_min[self.n], changes






